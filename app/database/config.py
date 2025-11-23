import os
import logging
from typing import Optional


class DatabaseConfig:
    DEFAULT_URL = "https://uqsmtnxrkkqyvydactjv.supabase.co"
    DEFAULT_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVxc210bnhya2txeXZ5ZGFjdGp2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM4Mjc3OTQsImV4cCI6MjA3OTQwMzc5NH0.-oWr41jUA9ZJAR3MdFEqyrhCme8F8qf1uix7n0tnrzI"

    @classmethod
    def get_supabase_url(cls) -> Optional[str]:
        url = os.getenv("SUPABASE_URL")
        if url and url.startswith("http"):
            return url
        return cls.DEFAULT_URL

    @classmethod
    def get_supabase_key(cls) -> Optional[str]:
        key = os.getenv("SUPABASE_ANON_KEY")
        if key:
            if key.startswith("ey"):
                return key
            logging.warning(
                "SUPABASE_ANON_KEY provided but does not look like a valid JWT."
            )
        key = os.getenv("SUPABASE_KEY")
        if key:
            if key.startswith("ey"):
                return key
            else:
                logging.warning(
                    "SUPABASE_KEY found but does not look like a valid JWT (starts with 'ey'). It might be a database password. Ignoring it to prevent connection errors."
                )
        logging.info("Using default public Supabase anon key.")
        return cls.DEFAULT_KEY

    @classmethod
    def get_database_url(cls) -> Optional[str]:
        """Get the direct PostgreSQL connection URL."""
        url = os.getenv("DATABASE_URL")
        if url:
            return url
        supabase_url = cls.get_supabase_url()
        db_password = os.getenv("SUPABASE_DB_PASSWORD")
        if supabase_url and db_password:
            try:
                if "//" in supabase_url:
                    project_ref = supabase_url.split("//")[1].split(".")[0]
                else:
                    project_ref = supabase_url.split(".")[0]
                if project_ref:
                    return f"postgresql://postgres:{db_password}@db.{project_ref}.supabase.co:5432/postgres"
            except Exception as e:
                logging.exception(f"Error constructing database URL: {e}")
        env_url = os.getenv("SUPABASE_URL")
        if env_url and env_url.startswith("postgresql://"):
            return env_url
        logging.warning(
            "Could not construct database URL. Ensure SUPABASE_DB_PASSWORD is set."
        )
        return None

    @classmethod
    def is_configured(cls) -> bool:
        return bool(cls.get_supabase_url() and cls.get_supabase_key())