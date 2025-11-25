import reflex as rx
import re
from app.states.cart_state import CartState
from app.services.mpesa_service import MpesaService


class CheckoutState(rx.State):
    name: str = ""
    email: str = ""
    phone: str = ""
    mpesa_phone: str = ""
    address: str = ""
    city: str = ""
    delivery_method: str = "Standard"
    payment_method: str = "M-Pesa"
    name_error: str = ""
    email_error: str = ""
    phone_error: str = ""
    address_error: str = ""
    is_processing_payment: bool = False

    @rx.var
    def delivery_fee(self) -> int:
        return 200 if self.delivery_method == "Express" else 0

    @rx.var
    async def final_total(self) -> int:
        cart_state = await self.get_state(CartState)
        return cart_state.total_price + self.delivery_fee

    @rx.event
    def set_delivery_method(self, method: str):
        self.delivery_method = method

    @rx.event
    def set_payment_method(self, method: str):
        self.payment_method = method
        if method == "M-Pesa" and (not self.mpesa_phone) and self.phone:
            self.mpesa_phone = self.phone

    @rx.event
    def set_field(self, field: str, value: str):
        setattr(self, field, value)
        setattr(self, f"{field}_error", "")

    @rx.event
    def validate(self) -> bool:
        valid = True
        if len(self.name) < 2:
            self.name_error = "Name is required"
            valid = False
        if not re.match("[^@]+@[^@]+\\.[^@]+", self.email):
            self.email_error = "Invalid email address"
            valid = False
        if len(self.phone) < 10:
            self.phone_error = "Valid phone number required"
            valid = False
        if len(self.address) < 5:
            self.address_error = "Address is required"
            valid = False
        return valid

    @rx.event
    async def place_order(self):
        if not self.validate():
            yield rx.toast.error("Please fix the errors in the form")
            return
        cart_state = await self.get_state(CartState)
        if not cart_state.items:
            yield rx.toast.error("Cart is empty")
            return
        if self.payment_method == "M-Pesa":
            if not self.mpesa_phone:
                yield rx.toast.error("Please enter M-Pesa phone number")
                return
            if not re.match("^(?:254|\\+254|0)?(?:(?:7|1)\\d{8})$", self.mpesa_phone):
                yield rx.toast.error("Invalid M-Pesa phone number format")
                return
        self.is_processing_payment = True
        yield
        import random
        import string
        from app.database.service import DatabaseService

        order_id = "PG-" + "".join(random.choices(string.digits, k=6))
        total_amount = cart_state.total_price + self.delivery_fee
        status = (
            "Pending Payment" if self.payment_method == "Manual M-Pesa" else "Pending"
        )
        order_data = {
            "id": order_id,
            "customer_email": self.email,
            "total_amount": total_amount,
            "status": status,
            "delivery_method": self.delivery_method,
            "payment_method": self.payment_method,
            "shipping_address": f"{self.address}, {self.city}",
            "contact_phone": self.phone,
            "checkout_request_id": None,
        }
        if self.payment_method == "M-Pesa":
            stk_response = MpesaService.initiate_stk_push(
                self.mpesa_phone, int(total_amount), order_id
            )
            if stk_response and stk_response.get("ResponseCode") == "0":
                order_data["checkout_request_id"] = stk_response.get(
                    "CheckoutRequestID"
                )
                rx.toast.info("M-Pesa STK Push sent! Please check your phone to pay.")
            else:
                self.is_processing_payment = False
                yield rx.toast.error(
                    "Failed to initiate M-Pesa payment. Please try again."
                )
                return
        elif self.payment_method == "Manual M-Pesa":
            pass
        items_data = []
        for item in cart_state.items:
            items_data.append(
                {
                    "product_id": item["id"],
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "price": item["price"],
                    "image": item.get("image", ""),
                }
            )
        result = await DatabaseService.create_order(order_data, items_data)
        self.is_processing_payment = False
        if result:
            cart_state.items = []
            yield rx.redirect(f"/order-confirmation?order_id={order_id}")
            return
        else:
            yield rx.toast.error("Failed to place order. Please try again.")
            return