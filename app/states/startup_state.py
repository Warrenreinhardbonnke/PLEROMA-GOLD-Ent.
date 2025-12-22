import reflex as rx
import logging
from app.database.service import DatabaseService
from app.database.seed import seed_database


class StartupState(rx.State):
    _is_initialized: bool = False

    @rx.event
    async def initialize_app(self):
        """
        Run application startup tasks.
        This ensures the database is initialized and seeded when the app launches.
        """
        if self._is_initialized:
            return
        try:
            logging.info("Starting application initialization...")
            await DatabaseService.initialize_tables()
            await seed_database()
            self._is_initialized = True
            logging.info("Application initialized successfully (DB + Seed).")
        except Exception as e:
            logging.exception(f"Startup initialization failed: {e}")