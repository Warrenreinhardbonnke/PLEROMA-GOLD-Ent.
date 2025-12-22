import asyncio
import logging
from app.database.service import DatabaseService
from app.data import products_data


async def seed_database():
    """Seed the database with initial data if empty."""
    print("Initializing Database...")
    await DatabaseService.initialize_tables()
    print("Checking database connection...")
    if not await DatabaseService.check_connection():
        print("❌ Database check failed after initialization attempt.")
        return
    print("Starting database seed...")
    try:
        existing_products = await DatabaseService.get_all_products()
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
            await DatabaseService.create_product(product_data)
        print("Seeding admin user...")
        admin_email = "admin@pleromagold.co.ke"
        if not await DatabaseService.get_customer_by_email(admin_email):
            await DatabaseService.create_customer(
                {
                    "email": admin_email,
                    "full_name": "System Administrator",
                    "role": "admin",
                }
            )
        print("Database seed completed successfully!")
    except Exception as e:
        logging.exception(f"❌ Failed to seed database: {e}")


if __name__ == "__main__":
    asyncio.run(seed_database())