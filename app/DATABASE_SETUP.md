
# PLEROMA GOLD - DATABASE SETUP & CONFIGURATION

This guide explains the database architecture and initialization procedures for the Pleroma Gold application.

## 1. Architecture Overview

The application uses a **Local SQLite Database** (`reflex.db`) as the default and only database option. This configuration is hardcoded in `rxconfig.py` to ensure stability and prevent any conflicts with external database URLs.

### Key Configuration Files:
*   **`rxconfig.py`**: Explicitly sets `db_url="sqlite:///reflex.db"` - this OVERRIDES any environment variables.
*   **`app/database/service.py`**: Handles all database operations using Reflex's native `rx.asession()`.
*   **`app/database/schema.py`**: Defines the SQLite-compatible SQL schema.
*   **`app/states/startup_state.py`**: Automatically initializes the database on first app load.

## 2. Why SQLite is Hardcoded

The database URL is explicitly set in `rxconfig.py` for the following reasons:

1. **Stability**: Eliminates external dependencies and connection issues.
2. **Simplicity**: No need to configure external database servers.
3. **Portability**: The database file travels with the application.
4. **Ignores REFLEX_DB_URL**: Any `REFLEX_DB_URL` environment variable is completely ignored.


# rxconfig.py - Database URL is HARDCODED
config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV3Plugin()],
    db_url="sqlite:///reflex.db",  # This overrides any environment variables
)


## 3. Automatic Initialization

The database is automatically initialized when the app first loads:

1. The `StartupState.initialize_app` event runs on the index page load.
2. It calls `seed_database()` which:
   - Creates all necessary tables if they don't exist.
   - Seeds initial product data if the database is empty.
   - Creates a default admin user.

**No manual setup is required!** Just run `reflex run` and the database will be ready.

## 4. Manual Initialization (Optional)

If you need to manually reset or initialize the database:

bash
python app/setup_database.py


**What this script does:**
1. Creates `reflex.db` in your project directory.
2. Executes the raw SQL from `app/database/schema.py` to create tables.
3. Seeds the database with sample products from `app/data.py`.
4. Creates a default Admin user (`admin@pleromagold.co.ke`).

## 5. Database Location

The SQLite database file is stored at:

your_project_root/reflex.db


## 6. Troubleshooting

### "OperationalError: no such table"
This error means the tables haven't been created yet:
1. The app should auto-initialize on first load.
2. If it doesn't, run: `python app/setup_database.py`

### "PostgreSQL connection refused" errors in logs
**These can be safely ignored.** The app is configured to use SQLite regardless of any PostgreSQL environment variables. The logs may show these errors if `REFLEX_DB_URL` is set in your environment, but they don't affect the app's functionality.

### To completely reset the database:
bash
rm reflex.db
python app/setup_database.py


## 7. Data Fallback

If database operations fail for any reason, the app automatically falls back to sample data from `app/data.py`. This ensures the app always displays products even if there are database issues.

