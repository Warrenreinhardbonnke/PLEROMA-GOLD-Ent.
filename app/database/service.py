import logging
from typing import Optional
import reflex as rx
from sqlalchemy import text


class DatabaseService:
    @staticmethod
    async def check_connection() -> bool:
        """Check if database connection is valid."""
        try:
            async with rx.asession() as session:
                await session.execute(text("SELECT 1"))
                return True
        except Exception as e:
            logging.exception(
                f"Database connection check failed (this is expected on first run): {e}"
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
            logging.exception(
                f"DB Error fetching products (falling back to sample data): {e}"
            )
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
            logging.exception(
                f"DB Error fetching product {product_id} (falling back to sample data): {e}"
            )
            from app.data import products_data

            for p in products_data:
                if p["id"] == product_id:
                    return p
            return None

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
            logging.exception(f"Error fetching stats (returning defaults): {e}")
            return {"revenue": 0, "orders": 0, "customers": 0}

    @staticmethod
    async def initialize_tables() -> bool:
        try:
            from app.database.schema import CREATE_TABLES_SQL

            async with rx.asession() as session:
                statements = [
                    s.strip() for s in CREATE_TABLES_SQL.split(";") if s.strip()
                ]
                for statement in statements:
                    await session.execute(text(statement))
                await session.commit()
                logging.info("Database tables initialized successfully.")
                return True
        except Exception as e:
            logging.exception(f"Error initializing tables: {e}")
            return False

    @staticmethod
    async def create_product(data: dict) -> bool:
        try:
            async with rx.asession() as session:
                await session.execute(
                    text("""
                        INSERT INTO products (name, price, image, rating, category, description, stock, status)
                        VALUES (:name, :price, :image, :rating, :category, :description, :stock, :status)
                    """),
                    data,
                )
                await session.commit()
                return True
        except Exception as e:
            logging.exception(f"Error creating product: {e}")
            return False

    @staticmethod
    async def create_customer(data: dict) -> bool:
        try:
            async with rx.asession() as session:
                await session.execute(
                    text("""
                        INSERT INTO customers (email, full_name, phone, role)
                        VALUES (:email, :full_name, :phone, :role)
                    """),
                    {
                        "email": data.get("email"),
                        "full_name": data.get("full_name"),
                        "phone": data.get("phone"),
                        "role": data.get("role", "customer"),
                    },
                )
                await session.commit()
                return True
        except Exception as e:
            logging.exception(f"Error creating customer: {e}")
            return False

    @staticmethod
    async def create_order(order_data: dict, items_data: list[dict]) -> bool:
        try:
            async with rx.asession() as session:
                await session.execute(
                    text("""
                        INSERT INTO orders (
                            id, customer_email, total_amount, status, delivery_method, 
                            payment_method, shipping_address, contact_phone, checkout_request_id
                        ) VALUES (
                            :id, :customer_email, :total_amount, :status, :delivery_method, 
                            :payment_method, :shipping_address, :contact_phone, :checkout_request_id
                        )
                    """),
                    order_data,
                )
                for item in items_data:
                    item["order_id"] = order_data["id"]
                    await session.execute(
                        text("""
                            INSERT INTO order_items (order_id, product_id, product_name, quantity, price, image)
                            VALUES (:order_id, :product_id, :name, :quantity, :price, :image)
                        """),
                        item,
                    )
                await session.commit()
                return True
        except Exception as e:
            logging.exception(f"Error creating order: {e}")
            return False

    @staticmethod
    async def update_order_by_checkout_id(checkout_id: str, updates: dict) -> bool:
        try:
            if not checkout_id or not updates:
                return False
            set_clauses = []
            params = {"checkout_id": checkout_id}
            for key, value in updates.items():
                set_clauses.append(f"{key} = :{key}")
                params[key] = value
            query = f"UPDATE orders SET {', '.join(set_clauses)} WHERE checkout_request_id = :checkout_id"
            async with rx.asession() as session:
                await session.execute(text(query), params)
                await session.commit()
                return True
        except Exception as e:
            logging.exception(f"Error updating order {checkout_id}: {e}")
            return False

    @staticmethod
    async def get_all_customers() -> list[dict]:
        try:
            async with rx.asession() as session:
                result = await session.execute(
                    text("SELECT * FROM customers ORDER BY created_at DESC")
                )
                return [dict(row._mapping) for row in result.fetchall()]
        except Exception as e:
            logging.exception(f"Error fetching customers: {e}")
            return []