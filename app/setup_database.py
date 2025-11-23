import sys
import os

sys.path.append(os.getcwd())
from app.database.service import DatabaseService
from app.database.schema import CREATE_TABLES_SQL
from app.database.seed import seed_database


def setup():
    print("""
--- PLEROMA GOLD DATABASE SETUP ---
""")
    print("1. Checking Supabase connection...")
    client = DatabaseService.get_client()
    if not client:
        print("❌ Failed to connect to Supabase.")
        print("Please check your settings in app/database/config.py")
        return
    print("✅ Connection established.")
    print("""
2. Checking for tables...""")
    if DatabaseService.check_connection():
        print("✅ Tables found. Proceeding to seed check.")
        seed_database()
    else:
        print("❌ Tables not found or not accessible.")
        print("""
*** ACTION REQUIRED ***""")
        print(
            "Supabase does not allow creating tables via the client API directly for security."
        )
        print("""Please go to your Supabase Dashboard -> SQL Editor and run the following SQL:
""")
        print("-" * 60)
        print(CREATE_TABLES_SQL)
        print("-" * 60)
        print("""
After running this SQL in Supabase, run this script again to seed data.""")


if __name__ == "__main__":
    setup()