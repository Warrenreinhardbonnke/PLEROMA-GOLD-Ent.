import reflex as rx
from typing import TypedDict


class AdminCustomer(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    total_orders: int
    total_spent: int
    join_date: str


class AdminCustomerState(rx.State):
    search_query: str = ""
    customers: list[AdminCustomer] = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+254 700 123 456",
            "total_orders": 12,
            "total_spent": 45000,
            "join_date": "2023-01-15",
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "+254 711 987 654",
            "total_orders": 5,
            "total_spent": 12500,
            "join_date": "2023-03-22",
        },
        {
            "id": 3,
            "name": "Michael Brown",
            "email": "michael@example.com",
            "phone": "+254 722 555 444",
            "total_orders": 3,
            "total_spent": 5600,
            "join_date": "2023-06-10",
        },
        {
            "id": 4,
            "name": "Sarah Wilson",
            "email": "sarah@example.com",
            "phone": "+254 733 222 111",
            "total_orders": 8,
            "total_spent": 28900,
            "join_date": "2023-02-05",
        },
        {
            "id": 5,
            "name": "David Miller",
            "email": "david@example.com",
            "phone": "+254 799 888 777",
            "total_orders": 1,
            "total_spent": 890,
            "join_date": "2023-10-20",
        },
    ]

    @rx.var
    def filtered_customers(self) -> list[AdminCustomer]:
        if not self.search_query:
            return self.customers
        query = self.search_query.lower()
        return [
            c
            for c in self.customers
            if query in c["name"].lower() or query in c["email"].lower()
        ]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query