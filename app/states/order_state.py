import reflex as rx
from typing import TypedDict


class OrderItem(TypedDict):
    name: str
    quantity: int
    image: str


class Order(TypedDict):
    id: str
    date: str
    status: str
    total: int
    payment_method: str
    items: list[OrderItem]


from app.database.service import DatabaseService


class OrderState(rx.State):
    selected_filter: str = "All Orders"
    orders: list[Order] = []

    @rx.event
    def on_load(self):
        pass

    @rx.var
    async def current_order(self) -> Order:
        order_id = self.router.page.params.get("order_id", "")
        if not order_id:
            return {"id": "", "date": "", "status": "", "total": 0, "items": []}
        for order in self.orders:
            if order["id"] == order_id:
                return order
        all_orders = await DatabaseService.get_all_orders()
        for order in all_orders:
            if order["id"] == order_id:
                items = await DatabaseService.get_order_items(order_id)
                mapped_order = {
                    "id": order["id"],
                    "date": str(order["created_at"])[:10],
                    "status": order["status"],
                    "total": order["total_amount"],
                    "payment_method": order.get("payment_method", ""),
                    "items": [
                        {
                            "name": i["product_name"],
                            "quantity": i["quantity"],
                            "image": i.get("image") or "/placeholder.svg",
                        }
                        for i in items
                    ],
                }
                return mapped_order
        return {
            "id": "",
            "date": "",
            "status": "",
            "total": 0,
            "payment_method": "",
            "items": [],
        }

    @rx.var
    def filtered_orders(self) -> list[Order]:
        if self.selected_filter == "All Orders":
            return self.orders
        return [o for o in self.orders if o["status"] == self.selected_filter]

    @rx.event
    def set_filter(self, filter_name: str):
        self.selected_filter = filter_name

    @rx.var
    def current_order(self) -> Order:
        order_id = self.router.page.params.get("order_id", "")
        for order in self.orders:
            if order["id"] == order_id:
                return order
        return Order(id="", date="", status="", total=0, payment_method="", items=[])