import reflex as rx
from typing import TypedDict


class CartItem(TypedDict):
    id: int
    name: str
    price: int
    image: str
    rating: int
    category: str
    description: str
    quantity: int


class CartState(rx.State):
    items: list[CartItem] = []
    discount_code: str = ""
    discount_amount: int = 0

    @rx.var
    def total_items(self) -> int:
        return sum((item.get("quantity", 1) for item in self.items))

    @rx.var
    def subtotal(self) -> int:
        return sum(
            (int(item["price"]) * item.get("quantity", 1) for item in self.items)
        )

    @rx.var
    def total_price(self) -> int:
        return self.subtotal - self.discount_amount

    @rx.event
    def add_to_cart(self, product: dict, quantity: int = 1):
        for item in self.items:
            if item["id"] == product["id"]:
                item["quantity"] = item.get("quantity", 1) + quantity
                self.items = self.items
                return rx.toast(
                    f"Updated quantity for {product['name']}",
                    duration=3000,
                    position="bottom-right",
                    close_button=True,
                )
        new_item = product.copy()
        new_item["quantity"] = quantity
        self.items.append(new_item)
        return rx.toast(
            f"Added {product['name']} to cart",
            duration=3000,
            position="bottom-right",
            close_button=True,
        )

    @rx.event
    def remove_from_cart(self, product_id: int):
        self.items = [item for item in self.items if item["id"] != product_id]

    @rx.event
    def increment_quantity(self, product_id: int):
        for item in self.items:
            if item["id"] == product_id:
                item["quantity"] = item.get("quantity", 1) + 1
        self.items = self.items

    @rx.event
    def decrement_quantity(self, product_id: int):
        for item in self.items:
            if item["id"] == product_id:
                if item.get("quantity", 1) > 1:
                    item["quantity"] = item.get("quantity", 1) - 1
        self.items = self.items

    @rx.event
    def set_discount_code(self, code: str):
        self.discount_code = code

    @rx.event
    def apply_discount(self):
        if self.discount_code.lower() == "pleromagold":
            self.discount_amount = int(self.subtotal * 0.1)
            return rx.toast("Discount applied!", duration=3000)
        else:
            self.discount_amount = 0
            return rx.toast("Invalid discount code", duration=3000)