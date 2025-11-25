import reflex as rx
from typing import TypedDict


class OrderItem(TypedDict):
    name: str
    quantity: int
    image: str


class AdminOrder(TypedDict):
    id: str
    customer: str
    date: str
    total: int
    status: str
    items: str
    payment_method: str
    receipt_number: str


from app.database.service import DatabaseService


class AdminOrderState(rx.State):
    filter_status: str = "All"
    status_options: list[str] = [
        "All",
        "Paid",
        "Pending",
        "Processing",
        "Delivered",
        "Cancelled",
    ]
    orders: list[AdminOrder] = []

    @rx.event
    async def on_load(self):
        db_orders = await DatabaseService.get_all_orders()
        self.orders = []
        for o in db_orders:
            self.orders.append(
                {
                    "id": o["id"],
                    "customer": o.get("customer_email") or "Unknown",
                    "date": str(o["created_at"])[:10],
                    "total": o["total_amount"],
                    "status": o["status"],
                    "items": o.get("items_summary", "Unknown items"),
                    "payment_method": o.get("payment_method") or "Unknown",
                    "receipt_number": o.get("mpesa_receipt_number") or "-",
                }
            )

    @rx.var
    def filtered_orders(self) -> list[AdminOrder]:
        if self.filter_status == "All":
            return self.orders
        return [o for o in self.orders if o["status"] == self.filter_status]

    @rx.event
    def set_filter(self, status: str):
        self.filter_status = status

    @rx.event
    async def update_status(self, order_id: str, new_status: str):
        if await DatabaseService.update_order_status(order_id, new_status):
            for order in self.orders:
                if order["id"] == order_id:
                    order["status"] = new_status
            return rx.toast.success(f"Order #{order_id} updated to {new_status}")
        return rx.toast.error("Failed to update order status")