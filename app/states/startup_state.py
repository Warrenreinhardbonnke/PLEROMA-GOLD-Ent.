import reflex as rx
import logging


class StartupState(rx.State):
    _is_initialized: bool = False

    @rx.event
    async def initialize_app(self):
        """
        Run application startup tasks.
        Initialize and seed database if needed.
        """
        if self._is_initialized:
            return
        try:
            logging.info("Application startup - initializing database...")
            from app.database.seed import seed_database

            await seed_database()
            self._is_initialized = True
            logging.info("Application initialized successfully.")
        except Exception as e:
            logging.exception(f"Startup initialization failed: {e}")