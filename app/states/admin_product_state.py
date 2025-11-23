import reflex as rx
from typing import TypedDict


class AdminProduct(TypedDict):
    id: int
    name: str
    category: str
    price: int
    stock: int
    status: str
    image: str


from app.database.service import DatabaseService


class AdminProductState(rx.State):
    search_query: str = ""
    products: list[AdminProduct] = []

    @rx.event
    def on_load(self):
        db_products = DatabaseService.get_all_products()
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
        if DatabaseService.delete_product(product_id):
            self.products = [p for p in self.products if p["id"] != product_id]
            return rx.toast.info("Product deleted successfully")
        return rx.toast.error("Failed to delete product")

    @rx.event
    def toggle_stock_status(self, product_id: int):
        for p in self.products:
            if p["id"] == product_id:
                new_stock = 0 if p["stock"] > 0 else 50
                new_status = "Out of Stock" if new_stock == 0 else "In Stock"
                DatabaseService.update_product(
                    product_id, {"stock": new_stock, "status": new_status}
                )
                p["stock"] = new_stock
                p["status"] = new_status
        return rx.toast.success("Stock status updated")