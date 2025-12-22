import reflex as rx
from typing import TypedDict


class MonthlySales(TypedDict):
    name: str
    sales: int
    revenue: int


class CategoryStat(TypedDict):
    name: str
    value: int
    color: str


from app.database.service import DatabaseService


class AdminState(rx.State):
    total_revenue: int = 0
    total_orders: int = 0
    total_customers: int = 0
    growth_rate: int = 12

    @rx.event
    async def on_load(self):
        stats = await DatabaseService.get_dashboard_stats()
        self.total_revenue = int(stats.get("revenue", 0))
        self.total_orders = int(stats.get("orders", 0))
        self.total_customers = int(stats.get("customers", 0))

    sales_data: list[MonthlySales] = [
        {"name": "Jan", "sales": 40, "revenue": 45000},
        {"name": "Feb", "sales": 30, "revenue": 35000},
        {"name": "Mar", "sales": 45, "revenue": 52000},
        {"name": "Apr", "sales": 50, "revenue": 61000},
        {"name": "May", "sales": 65, "revenue": 75000},
        {"name": "Jun", "sales": 80, "revenue": 92000},
    ]
    category_data: list[CategoryStat] = [
        {"name": "Fried", "value": 400, "color": "#DAA520"},
        {"name": "Roasted", "value": 300, "color": "#8B4513"},
        {"name": "Honey", "value": 300, "color": "#F5DEB3"},
        {"name": "Butter", "value": 200, "color": "#D2691E"},
    ]
    recent_activity: list[dict] = [
        {"action": "New order #PG-83924", "time": "5 mins ago"},
        {"action": "New customer registered", "time": "1 hour ago"},
        {"action": "Restocked Fried Groundnuts", "time": "2 hours ago"},
        {"action": "Order #PG-83920 delivered", "time": "3 hours ago"},
    ]

    @rx.var
    def revenue_formatted(self) -> str:
        return f"KES {self.total_revenue:,}"