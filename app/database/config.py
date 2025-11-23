import os
from typing import Optional


class DatabaseConfig:
    @classmethod
    def get_supabase_url(cls) -> Optional[str]:
        return os.getenv("SUPABASE_URL")

    @classmethod
    def get_supabase_key(cls) -> Optional[str]:
        return os.getenv("SUPABASE_KEY")

    @classmethod
    def is_configured(cls) -> bool:
        return bool(cls.get_supabase_url() and cls.get_supabase_key())