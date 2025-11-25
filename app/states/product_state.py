import reflex as rx
import logging
from typing import TypedDict
from app.data import products_data
from app.database.service import DatabaseService
from app.database.seed import seed_database


class Product(TypedDict):
    id: int
    name: str
    price: int
    image: str
    rating: int
    category: str
    description: str


class ProductState(rx.State):
    products: list[Product] = products_data
    search_query: str = ""
    selected_category: str = "All"
    sort_option: str = "Popularity"
    quantity: int = 1
    selected_size: str = "250g"
    size_options: list[str] = ["250g", "500g", "1kg"]

    @rx.event
    async def on_load(self):
        """Initialize DB and fetch products."""
        try:
            db_products = await DatabaseService.get_all_products()
            if db_products:
                self.products = db_products
        except Exception as e:
            logging.exception(f"Failed to load products from DB: {e}")

    @rx.var
    def featured_products(self) -> list[Product]:
        return self.products[:6]

    @rx.var
    def categories(self) -> list[str]:
        unique_categories = set((p["category"] for p in self.products))
        return ["All"] + sorted(list(unique_categories))

    @rx.var
    def filtered_products(self) -> list[Product]:
        products = self.products
        if self.selected_category != "All":
            products = [p for p in products if p["category"] == self.selected_category]
        if self.search_query:
            query = self.search_query.lower()
            products = [
                p
                for p in products
                if query in p["name"].lower() or query in p["description"].lower()
            ]
        if self.sort_option == "Price: Low to High":
            products = sorted(products, key=lambda p: p["price"])
        elif self.sort_option == "Price: High to Low":
            products = sorted(products, key=lambda p: p["price"], reverse=True)
        elif self.sort_option == "Newest":
            products = sorted(products, key=lambda p: p["id"], reverse=True)
        return products

    @rx.var
    def current_product(self) -> dict:
        """Get the product for the current detail page."""
        params = self.router.page.params
        product_id_str = params.get("id", "")
        if not product_id_str:
            return {}
        try:
            product_id = int(product_id_str)
            for p in self.products:
                if p["id"] == product_id:
                    return p
        except ValueError as e:
            logging.exception(f"Error parsing product id: {e}")
            return {}
        return {}

    @rx.var
    def related_products(self) -> list[Product]:
        """Get related products based on current product category."""
        current = self.current_product
        if not current:
            return []
        category = current.get("category")
        pid = current.get("id")
        related = [
            p for p in self.products if p["category"] == category and p["id"] != pid
        ]
        return related[:4]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_category(self, category: str):
        self.selected_category = category

    @rx.event
    def set_sort_option(self, option: str):
        self.sort_option = option

    @rx.event
    def increment_quantity(self):
        self.quantity += 1

    @rx.event
    def decrement_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1

    @rx.event
    def set_size(self, size: str):
        self.selected_size = size

    @rx.event
    def reset_detail_state(self):
        self.quantity = 1
        self.selected_size = "250g"