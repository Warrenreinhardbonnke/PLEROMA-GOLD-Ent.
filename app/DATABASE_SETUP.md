# PLEROMA GOLD - DATABASE SETUP & CONFIGURATION

This guide explains the database architecture and initialization procedures for the Pleroma Gold application.

## 1. Architecture Overview

The application is configured to use a **Local SQLite Database** (`reflex.db`) by default. This ensures stability and eliminates external dependencies during development.

*   **`rxconfig.py`**: Explicitly sets the `db_url` to `sqlite:///reflex.db`.
*   **`app/database/service.py`**: Handles database operations using Reflex's native `rx.asession()`.
*   **`app/database/schema.py`**: Defines the SQLite-compatible SQL schema.
*   **`app/setup_database.py`**: Entry point script for initializing the database.

## 2. Initialization Steps

Before running the app for the first time, you must initialize the database tables and seed initial data.

### Step 1: Run the Setup Script

Run this command from the project root to create the local database file and tables:

bash
python app/setup_database.py


**What this script does:**
1.  Creates `reflex.db` in your project directory.
2.  Executes the raw SQL from `app/database/schema.py` to create tables.
3.  Seeds the database with sample products from `app/data.py`.
4.  Creates a default Admin user (`admin@pleromagold.co.ke`).

### Step 2: Verify Installation

Check the logs output by the script. You should see:

text
Initializing Database...
Database tables initialized.
Checking database connection...
Starting database seed...
Seeding products...
Seeding admin user...
Database seed completed successfully!


## 3. Troubleshooting

### "Database tables not initialized" or "OperationalError"
If you encounter errors stating that tables are missing:
1.  Ensure you have run `python app/setup_database.py`.
2.  Check if `reflex.db` exists in your project root.
3.  If issues persist, delete `reflex.db` and run the setup script again.
