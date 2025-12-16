import reflex as rx
import logging


class StartupState(rx.State):
    _is_initialized: bool = False

    @rx.event
    async def initialize_app(self):
        """
        Run application startup tasks.
        Initialize and seed database if needed.
        This runs automatically on the first page load.
        """
        if self._is_initialized:
            return
        try:
            logging.info("Application startup - initializing database with SQLite...")
            from app.database.seed import seed_database

            await seed_database()
            self._is_initialized = True
            logging.info("Application initialized successfully with SQLite database.")
        except Exception as e:
            logging.exception(
                f"Startup initialization warning (app will use fallback data): {e}"
            )
            self._is_initialized = True