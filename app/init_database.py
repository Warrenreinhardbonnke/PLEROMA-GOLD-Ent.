import os
import logging
import psycopg
from app.database.config import DatabaseConfig
from app.database.schema import CREATE_TABLES_SQL
from app.data import products_data

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_db_connection():
    """Establish a connection to the database using psycopg."""
    db_url = DatabaseConfig.get_database_url()
    if not db_url:
        logging.error("DATABASE_URL not found in environment variables.")
        logging.error(
            "Please set DATABASE_URL or (SUPABASE_URL and SUPABASE_DB_PASSWORD)."
        )
        return None
    try:
        logging.info("Connecting to database...")
        conn = psycopg.connect(db_url, autocommit=True)
        return conn
    except Exception as e:
        logging.exception(f"Failed to connect to database: {e}")
        return None


def init_schema(conn):
    """Initialize the database schema."""
    try:
        logging.info("Creating tables if they don't exist...")
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLES_SQL)
        logging.info("Schema initialization completed successfully.")
        return True
    except Exception as e:
        logging.exception(f"Failed to initialize schema: {e}")
        return False


def seed_data(conn):
    """Seed initial data into the database."""
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM products")
            count = cur.fetchone()[0]
            if count > 0:
                logging.info(
                    f"Products table already has {count} items. Skipping product seed."
                )
            else:
                logging.info("Seeding products...")
                for p in products_data:
                    cur.execute(
                        """
                        INSERT INTO products 
                        (name, price, image, rating, category, description, stock, status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            p["name"],
                            p["price"],
                            p["image"],
                            p.get("rating", 5),
                            p.get("category", "General"),
                            p.get("description", ""),
                            50,
                            "In Stock",
                        ),
                    )
                logging.info(f"Seeded {len(products_data)} products.")
            admin_email = "admin@pleromagold.co.ke"
            cur.execute("SELECT id FROM customers WHERE email = %s", (admin_email,))
            if cur.fetchone():
                logging.info("Admin user already exists.")
            else:
                logging.info("Creating admin user...")
                cur.execute(
                    """
                    INSERT INTO customers (email, full_name, role)
                    VALUES (%s, %s, %s)
                    """,
                    (admin_email, "System Administrator", "admin"),
                )
                logging.info("Admin user created.")
        return True
    except Exception as e:
        logging.exception(f"Failed to seed data: {e}")
        return False


def main():
    """Main initialization routine."""
    print("=" * 50)
    print("PLEROMA GOLD - DATABASE INITIALIZATION")
    print("=" * 50)
    conn = get_db_connection()
    if not conn:
        print("""
CRITICAL ERROR: Could not connect to database.""")
        print("Make sure you have configured your environment variables correctly.")
        return
    try:
        if init_schema(conn):
            print("✅ Database schema initialized.")
            if seed_data(conn):
                print("✅ Initial data seeded.")
                print("""
Database setup completed successfully!""")
            else:
                print("❌ Data seeding failed.")
        else:
            print("❌ Schema initialization failed.")
    finally:
        conn.close()
        logging.info("Database connection closed.")


if __name__ == "__main__":
    main()