import logging
from typing import Optional
from supabase import create_client, Client
from app.database.config import DatabaseConfig


class SupabaseDB:
    _client: Optional[Client] = None

    @classmethod
    def get_client(cls) -> Optional[Client]:
        if cls._client is None:
            url = DatabaseConfig.get_supabase_url()
            key = DatabaseConfig.get_supabase_key()
            if not url or not key:
                logging.warning("Supabase URL or Key not configured.")
                return None
            try:
                cls._client = create_client(url, key)
                if cls._client:
                    logging.info(f"Supabase client initialized for {url}")
            except Exception as e:
                logging.exception(f"Failed to initialize Supabase client: {e}")
                return None
        return cls._client