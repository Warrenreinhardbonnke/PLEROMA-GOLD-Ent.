import sys
import os
import asyncio

sys.path.append(os.getcwd())
from app.database.service import DatabaseService
from app.database.seed import seed_database


async def verify():
    print("🔍 Verifying Database Configuration...")
    print("1. Checking Connection...")
    if await DatabaseService.check_connection():
        print("   ✅ Connection Successful (Tables exist)")
    else:
        print(
            "   ℹ️  Tables not found or connection issue, attempting initialization..."
        )
    print("2. Initializing/Updating Tables...")
    if await DatabaseService.initialize_tables():
        print("   ✅ Tables Initialized")
    else:
        print("   ❌ Failed to initialize tables")
        return
    print("3. Seeding Data...")
    await seed_database()
    print("4. Verifying Data...")
    products = await DatabaseService.get_all_products()
    print(f"   ✅ Found {len(products)} products")
    if len(products) > 0:
        print(f"   First product: {products[0]['name']}")
    print("""
🎉 Database configuration verified!""")


if __name__ == "__main__":
    asyncio.run(verify())