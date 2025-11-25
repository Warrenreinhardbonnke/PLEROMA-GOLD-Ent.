import sys
import os
import asyncio
import logging

sys.path.append(os.getcwd())
from app.database.seed import seed_database


def setup():
    print("""
--- PLEROMA GOLD DATABASE SETUP ---
""")
    print("Initializing Local SQLite Database (reflex.db)...")
    try:
        asyncio.run(seed_database())
        print("""
✅ Setup process finished successfully.""")
    except Exception as e:
        logging.exception(f"Setup process failed: {e}")
        print(f"\n❌ Setup process failed: {e}")


if __name__ == "__main__":
    setup()