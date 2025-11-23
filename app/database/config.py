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
        return os.getenv("SUPABASE_KEY", cls.DEFAULT_KEY)

    @classmethod
    def get_database_url(cls) -> Optional[str]:
        """Get the direct PostgreSQL connection URL."""
        url = os.getenv("DATABASE_URL")
        if url:
            return url
        supabase_url = cls.get_supabase_url()
        db_password = os.getenv("SUPABASE_DB_PASSWORD")
        if supabase_url and db_password and ("supabase.co" in supabase_url):
            try:
                project_ref = supabase_url.split("//")[1].split(".")[0]
                return f"postgresql://postgres:{db_password}@db.{project_ref}.supabase.co:5432/postgres"
            except IndexError:
                logging.exception(
                    "Failed to parse Supabase URL for database connection"
                )
                return None
        return None

    @classmethod
    def is_configured(cls) -> bool:
        return bool(cls.get_supabase_url() and cls.get_supabase_key())