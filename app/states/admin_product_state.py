import reflex as rx
from typing import TypedDict
from app.database.service import DatabaseService


class AdminProduct(TypedDict):
    id: int
    name: str
    category: str
    price: int
    stock: int
    status: str
    image: str


class AdminProductState(rx.State):
    search_query: str = ""
    products: list[AdminProduct] = []

    @rx.event(background=True)
    async def on_load(self):
        async with self:
            pass
        db_products = await DatabaseService.get_all_products()
        async with self:
            if db_products:
                self.products = db_products

    @rx.var
    def filtered_products(self) -> list[AdminProduct]:
        if not self.search_query:
            return self.products
        query = self.search_query.lower()
        return [
            p
            for p in self.products
            if query in p["name"].lower() or query in p["category"].lower()
        ]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def delete_product(self, product_id: int):
        self.products = [p for p in self.products if p["id"] != product_id]
        return rx.toast.info("Product removed from view")

    @rx.event
    def toggle_stock_status(self, product_id: int):
        for p in self.products:
            if p["id"] == product_id:
                new_stock = 0 if p["stock"] > 0 else 50
                new_status = "Out of Stock" if new_stock == 0 else "In Stock"
                p["stock"] = new_stock
                p["status"] = new_status
        return rx.toast.success("Stock status updated")