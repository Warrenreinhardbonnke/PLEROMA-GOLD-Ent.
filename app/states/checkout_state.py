import reflex as rx
import re
from app.states.cart_state import CartState


class CheckoutState(rx.State):
    name: str = ""
    email: str = ""
    phone: str = ""
    address: str = ""
    city: str = ""
    delivery_method: str = "Standard"
    payment_method: str = "M-Pesa"
    name_error: str = ""
    email_error: str = ""
    phone_error: str = ""
    address_error: str = ""

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
            return rx.toast.error("Please fix the errors in the form")
        cart_state = await self.get_state(CartState)
        if not cart_state.items:
            return rx.toast.error("Cart is empty")
        import random
        import string
        from app.database.service import DatabaseService

        order_id = "PG-" + "".join(random.choices(string.digits, k=6))
        order_data = {
            "id": order_id,
            "customer_email": self.email,
            "total_amount": cart_state.total_price + self.delivery_fee,
            "status": "Pending",
            "delivery_method": self.delivery_method,
            "payment_method": self.payment_method,
            "shipping_address": f"{self.address}, {self.city}",
            "contact_phone": self.phone,
        }
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
        result = DatabaseService.create_order(order_data, items_data)
        if result:
            cart_state.items = []
            return rx.redirect(f"/order-confirmation?order_id={order_id}")
        else:
            return rx.toast.error("Failed to place order. Please try again.")