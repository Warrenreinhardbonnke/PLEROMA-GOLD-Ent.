import logging
from typing import Optional
import reflex as rx
from sqlalchemy import text
from app.database.schema import CREATE_TABLES_SQL


class DatabaseService:
    @staticmethod
    async def initialize_tables():
        """Initialize database tables via raw SQL."""
        try:
            async with rx.asession() as session:
                await session.execute(text("PRAGMA foreign_keys = ON;"))
                statements = CREATE_TABLES_SQL.split(";")
                for stmt in statements:
                    if stmt.strip():
                        await session.execute(text(stmt))
                await session.commit()
            logging.info("Database tables initialized.")
            return True
        except Exception as e:
            logging.exception(
                f"Failed to initialize tables. Ensure 'db_url' in rxconfig.py is set to 'sqlite:///reflex.db' and not using Postgres env vars. Error: {e}"
            )
            return False

    @staticmethod
    async def check_connection() -> bool:
        """Check if database connection is valid and tables exist."""
        try:
            async with rx.asession() as session:
                await session.execute(text("SELECT 1"))
                result = await session.execute(
                    text(
                        "SELECT name FROM sqlite_master WHERE type='table' AND name='products'"
                    )
                )
                return result.fetchone() is not None
        except Exception as e:
            logging.exception(
                f"Database connection check failed. Verify 'db_url' in rxconfig.py is 'sqlite:///reflex.db'. Error: {e}"
            )
            return False

    @staticmethod
    async def get_all_products() -> list[dict]:
        try:
            async with rx.asession() as session:
                result = await session.execute(
                    text("SELECT * FROM products ORDER BY id")
                )
                return [dict(row._mapping) for row in result.fetchall()]
        except Exception as e:
            logging.exception(f"DB Error fetching products: {e}")
            from app.data import products_data

            return products_data

    @staticmethod
    async def get_product_by_id(product_id: int) -> Optional[dict]:
        try:
            async with rx.asession() as session:
                result = await session.execute(
                    text("SELECT * FROM products WHERE id = :id"), {"id": product_id}
                )
                row = result.fetchone()
                return dict(row._mapping) if row else None
        except Exception as e:
            logging.exception(f"DB Error fetching product {product_id}: {e}")
            from app.data import products_data

            for p in products_data:
                if p["id"] == product_id:
                    return p
            return None

    @staticmethod
    async def create_product(product_data: dict) -> Optional[dict]:
        try:
            async with rx.asession() as session:
                columns = ", ".join(product_data.keys())
                placeholders = ", ".join((f":{k}" for k in product_data.keys()))
                query = text(
                    f"INSERT INTO products ({columns}) VALUES ({placeholders}) RETURNING *"
                )
                result = await session.execute(query, product_data)
                await session.commit()
                row = result.fetchone()
                return dict(row._mapping) if row else None
        except Exception as e:
            logging.exception(f"Error creating product: {e}")
            return None

    @staticmethod
    async def update_product(product_id: int, updates: dict) -> Optional[dict]:
        try:
            if not updates:
                return await DatabaseService.get_product_by_id(product_id)
            set_clause = ", ".join((f"{k} = :{k}" for k in updates.keys()))
            params = {**updates, "id": product_id}
            async with rx.asession() as session:
                result = await session.execute(
                    text(
                        f"UPDATE products SET {set_clause} WHERE id = :id RETURNING *"
                    ),
                    params,
                )
                await session.commit()
                row = result.fetchone()
                return dict(row._mapping) if row else None
        except Exception as e:
            logging.exception(f"Error updating product {product_id}: {e}")
            return None

    @staticmethod
    async def delete_product(product_id: int) -> bool:
        try:
            async with rx.asession() as session:
                await session.execute(text("PRAGMA foreign_keys = ON;"))
                await session.execute(
                    text("DELETE FROM products WHERE id = :id"), {"id": product_id}
                )
                await session.commit()
            return True
        except Exception as e:
            logging.exception(f"Error deleting product {product_id}: {e}")
            return False

    @staticmethod
    async def get_customer_by_email(email: str) -> Optional[dict]:
        try:
            async with rx.asession() as session:
                result = await session.execute(
                    text("SELECT * FROM customers WHERE email = :email"),
                    {"email": email},
                )
                row = result.fetchone()
                return dict(row._mapping) if row else None
        except Exception as e:
            logging.exception(f"Error fetching customer {email}: {e}")
            return None

    @staticmethod
    async def create_customer(customer_data: dict) -> Optional[dict]:
        try:
            async with rx.asession() as session:
                columns = ", ".join(customer_data.keys())
                placeholders = ", ".join((f":{k}" for k in customer_data.keys()))
                result = await session.execute(
                    text(
                        f"INSERT INTO customers ({columns}) VALUES ({placeholders}) RETURNING *"
                    ),
                    customer_data,
                )
                await session.commit()
                row = result.fetchone()
                return dict(row._mapping) if row else None
        except Exception as e:
            logging.exception(f"Error creating customer: {e}")
            return None

    @staticmethod
    async def create_order(order_data: dict, items: list[dict]) -> Optional[dict]:
        try:
            async with rx.asession() as session:
                columns = ", ".join(order_data.keys())
                placeholders = ", ".join((f":{k}" for k in order_data.keys()))
                order_res = await session.execute(
                    text(
                        f"INSERT INTO orders ({columns}) VALUES ({placeholders}) RETURNING *"
                    ),
                    order_data,
                )
                order_row = order_res.fetchone()
                order = dict(order_row._mapping) if order_row else order_data
                if items:
                    for item in items:
                        item_data = {
                            "order_id": order["id"],
                            "product_id": item.get("product_id"),
                            "product_name": item.get("product_name")
                            or item.get("name"),
                            "quantity": item.get("quantity"),
                            "price": item.get("price"),
                            "image": item.get("image"),
                        }
                        cols = ", ".join(item_data.keys())
                        vals = ", ".join((f":{k}" for k in item_data.keys()))
                        await session.execute(
                            text(f"INSERT INTO order_items ({cols}) VALUES ({vals})"),
                            item_data,
                        )
                await session.commit()
                return order
        except Exception as e:
            logging.exception(f"Failed to create order in DB: {e}")
            return order_data

    @staticmethod
    async def get_order_items(order_id: str) -> list[dict]:
        try:
            async with rx.asession() as session:
                result = await session.execute(
                    text("SELECT * FROM order_items WHERE order_id = :order_id"),
                    {"order_id": order_id},
                )
                return [dict(row._mapping) for row in result.fetchall()]
        except Exception as e:
            logging.exception(f"Error fetching items for order {order_id}: {e}")
            return []

    @staticmethod
    async def get_orders_by_user(user_email: str) -> list[dict]:
        try:
            async with rx.asession() as session:
                orders_res = await session.execute(
                    text(
                        "SELECT * FROM orders WHERE customer_email = :email ORDER BY created_at DESC"
                    ),
                    {"email": user_email},
                )
                orders = [dict(row._mapping) for row in orders_res.fetchall()]
                for order in orders:
                    items_res = await session.execute(
                        text("SELECT * FROM order_items WHERE order_id = :oid"),
                        {"oid": order["id"]},
                    )
                    order["items"] = [dict(r._mapping) for r in items_res.fetchall()]
                return orders
        except Exception as e:
            logging.exception(f"Error fetching orders for {user_email}: {e}")
            return []

    @staticmethod
    async def get_all_orders() -> list[dict]:
        try:
            async with rx.asession() as session:
                orders_res = await session.execute(
                    text("SELECT * FROM orders ORDER BY created_at DESC")
                )
                orders = [dict(row._mapping) for row in orders_res.fetchall()]
                for order in orders:
                    items_res = await session.execute(
                        text("SELECT * FROM order_items WHERE order_id = :oid"),
                        {"oid": order["id"]},
                    )
                    items = [dict(r._mapping) for r in items_res.fetchall()]
                    order["items_summary"] = ", ".join(
                        [f"{i['quantity']}x {i['product_name']}" for i in items]
                    )
                    order["items_count"] = sum((i["quantity"] for i in items))
                    order["order_items"] = items
                return orders
        except Exception as e:
            logging.exception(f"Error fetching all orders: {e}")
            return []

    @staticmethod
    async def update_order_status(order_id: str, status: str) -> bool:
        try:
            async with rx.asession() as session:
                await session.execute(
                    text("UPDATE orders SET status = :status WHERE id = :id"),
                    {"status": status, "id": order_id},
                )
                await session.commit()
            return True
        except Exception as e:
            logging.exception(f"Error updating order {order_id}: {e}")
            return False

    @staticmethod
    async def update_order_by_checkout_id(checkout_id: str, updates: dict) -> bool:
        try:
            if not updates:
                return True
            set_clause = ", ".join((f"{k} = :{k}" for k in updates.keys()))
            params = {**updates, "cid": checkout_id}
            async with rx.asession() as session:
                await session.execute(
                    text(
                        f"UPDATE orders SET {set_clause} WHERE checkout_request_id = :cid"
                    ),
                    params,
                )
                await session.commit()
            return True
        except Exception as e:
            logging.exception(f"Error updating order by checkout_id {checkout_id}: {e}")
            return False

    @staticmethod
    async def get_dashboard_stats() -> dict:
        try:
            async with rx.asession() as session:
                orders_res = await session.execute(text("SELECT count(*) FROM orders"))
                orders_count = orders_res.scalar() or 0
                cust_res = await session.execute(text("SELECT count(*) FROM customers"))
                customers_count = cust_res.scalar() or 0
                rev_res = await session.execute(
                    text("SELECT sum(total_amount) FROM orders")
                )
                total_revenue = rev_res.scalar() or 0
                return {
                    "revenue": total_revenue,
                    "orders": orders_count,
                    "customers": customers_count,
                }
        except Exception as e:
            logging.exception(f"Error fetching stats: {e}")
            return {"revenue": 0, "orders": 0, "customers": 0}