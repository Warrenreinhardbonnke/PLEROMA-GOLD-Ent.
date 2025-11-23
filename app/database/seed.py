import logging
from app.database.service import DatabaseService
from app.data import products_data


def seed_database():
    """Seed the database with initial data if empty."""
    print("Initializing Database Check...")
    if not DatabaseService.check_connection():
        print("❌ Database check failed.")
        print(
            "If the tables are missing, please read SUPABASE_SETUP.md for manual setup instructions."
        )
        return
    print("Starting database seed...")
    existing_products = DatabaseService.get_all_products()
    if existing_products and len(existing_products) > 0:
        print(
            f"Database already contains {len(existing_products)} products. Skipping seed."
        )
        return
    print("Seeding products...")
    for p in products_data:
        product_data = {
            "name": p["name"],
            "price": p["price"],
            "image": p["image"],
            "rating": p["rating"],
            "category": p["category"],
            "description": p["description"],
            "stock": 50,
            "status": "In Stock",
        }
        DatabaseService.create_product(product_data)
    print("Seeding admin user...")
    admin_email = "admin@pleromagold.co.ke"
    if not DatabaseService.get_customer_by_email(admin_email):
        DatabaseService.create_customer(
            {"email": admin_email, "full_name": "System Administrator", "role": "admin"}
        )
    print("Database seed completed successfully!")


if __name__ == "__main__":
    seed_database()