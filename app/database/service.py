import logging
from typing import Optional
from app.database.client import SupabaseDB


class DatabaseService:
    @staticmethod
    def get_client():
        return SupabaseDB.get_client()

    @staticmethod
    def check_connection() -> bool:
        """Check if database connection is valid and tables exist."""
        client = DatabaseService.get_client()
        if not client:
            return False
        try:
            client.table("products").select("count", count="exact", head=True).execute()
            return True
        except Exception as e:
            logging.exception(f"Database check failed: {e}")
            return False

    @staticmethod
    def get_all_products() -> list[dict]:
        client = DatabaseService.get_client()
        if not client:
            return []
        try:
            response = client.table("products").select("*").order("id").execute()
            return response.data
        except Exception as e:
            logging.exception(f"Error fetching products: {e}")
            return []

    @staticmethod
    def get_product_by_id(product_id: int) -> Optional[dict]:
        client = DatabaseService.get_client()
        if not client:
            return None
        try:
            response = (
                client.table("products")
                .select("*")
                .eq("id", product_id)
                .single()
                .execute()
            )
            return response.data
        except Exception as e:
            logging.exception(f"Error fetching product {product_id}: {e}")
            return None

    @staticmethod
    def create_product(product_data: dict) -> Optional[dict]:
        client = DatabaseService.get_client()
        if not client:
            return None
        try:
            response = client.table("products").insert(product_data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            logging.exception(f"Error creating product: {e}")
            return None

    @staticmethod
    def update_product(product_id: int, updates: dict) -> Optional[dict]:
        client = DatabaseService.get_client()
        if not client:
            return None
        try:
            response = (
                client.table("products").update(updates).eq("id", product_id).execute()
            )
            return response.data[0] if response.data else None
        except Exception as e:
            logging.exception(f"Error updating product {product_id}: {e}")
            return None

    @staticmethod
    def delete_product(product_id: int) -> bool:
        client = DatabaseService.get_client()
        if not client:
            return False
        try:
            client.table("products").delete().eq("id", product_id).execute()
            return True
        except Exception as e:
            logging.exception(f"Error deleting product {product_id}: {e}")
            return False

    @staticmethod
    def get_customer_by_email(email: str) -> Optional[dict]:
        client = DatabaseService.get_client()
        if not client:
            return None
        try:
            response = (
                client.table("customers")
                .select("*")
                .eq("email", email)
                .maybe_single()
                .execute()
            )
            return response.data
        except Exception as e:
            logging.exception(f"Error fetching customer {email}: {e}")
            return None

    @staticmethod
    def create_customer(customer_data: dict) -> Optional[dict]:
        client = DatabaseService.get_client()
        if not client:
            return None
        try:
            response = client.table("customers").insert(customer_data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            logging.exception(f"Error creating customer: {e}")
            return None

    @staticmethod
    def create_order(order_data: dict, items: list[dict]) -> Optional[dict]:
        client = DatabaseService.get_client()
        if not client:
            return None
        try:
            order_res = client.table("orders").insert(order_data).execute()
            if not order_res.data:
                raise Exception("Failed to create order record")
            order = order_res.data[0]
            order_id = order["id"]
            items_data = []
            for item in items:
                items_data.append(
                    {
                        "order_id": order_id,
                        "product_id": item.get("product_id"),
                        "product_name": item.get("name"),
                        "quantity": item.get("quantity"),
                        "price": item.get("price"),
                        "image": item.get("image"),
                    }
                )
            if items_data:
                client.table("order_items").insert(items_data).execute()
            return order
        except Exception as e:
            logging.exception(f"Failed to create order: {e}")
            return None

    @staticmethod
    def get_order_items(order_id: str) -> list[dict]:
        client = DatabaseService.get_client()
        if not client:
            return []
        try:
            response = (
                client.table("order_items")
                .select("*")
                .eq("order_id", order_id)
                .execute()
            )
            return response.data
        except Exception as e:
            logging.exception(f"Error fetching items for order {order_id}: {e}")
            return []

    @staticmethod
    def get_orders_by_user(user_email: str) -> list[dict]:
        client = DatabaseService.get_client()
        if not client:
            return []
        try:
            response = (
                client.table("orders")
                .select("*, order_items(*)")
                .eq("customer_email", user_email)
                .order("created_at", desc=True)
                .execute()
            )
            orders = response.data
            for order in orders:
                order["items"] = order.get("order_items", [])
            return orders
        except Exception as e:
            logging.exception(f"Error fetching orders for {user_email}: {e}")
            return []

    @staticmethod
    def get_all_orders() -> list[dict]:
        client = DatabaseService.get_client()
        if not client:
            return []
        try:
            response = (
                client.table("orders")
                .select("*, order_items(*)")
                .order("created_at", desc=True)
                .execute()
            )
            orders = response.data
            for order in orders:
                items = order.get("order_items", [])
                order["items_summary"] = ", ".join(
                    [f"{i['quantity']}x {i['product_name']}" for i in items]
                )
                order["items_count"] = sum((i["quantity"] for i in items))
            return orders
        except Exception as e:
            logging.exception(f"Error fetching all orders: {e}")
            return []

    @staticmethod
    def update_order_status(order_id: str, status: str) -> bool:
        client = DatabaseService.get_client()
        if not client:
            return False
        try:
            client.table("orders").update({"status": status}).eq(
                "id", order_id
            ).execute()
            return True
        except Exception as e:
            logging.exception(f"Error updating order {order_id}: {e}")
            return False

    @staticmethod
    def update_order_by_checkout_id(checkout_id: str, updates: dict) -> bool:
        client = DatabaseService.get_client()
        if not client:
            return False
        try:
            client.table("orders").update(updates).eq(
                "checkout_request_id", checkout_id
            ).execute()
            return True
        except Exception as e:
            logging.exception(f"Error updating order by checkout_id {checkout_id}: {e}")
            return False

    @staticmethod
    def get_dashboard_stats() -> dict:
        client = DatabaseService.get_client()
        if not client:
            return {"revenue": 0, "orders": 0, "customers": 0}
        try:
            orders_count = (
                client.table("orders")
                .select("*", count="exact", head=True)
                .execute()
                .count
            )
            customers_count = (
                client.table("customers")
                .select("*", count="exact", head=True)
                .execute()
                .count
            )
            revenue_data = client.table("orders").select("total_amount").execute()
            total_revenue = sum((item["total_amount"] for item in revenue_data.data))
            return {
                "revenue": total_revenue,
                "orders": orders_count or 0,
                "customers": customers_count or 0,
            }
        except Exception as e:
            logging.exception(f"Error fetching stats: {e}")
            return {"revenue": 0, "orders": 0, "customers": 0}