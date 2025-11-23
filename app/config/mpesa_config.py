import os


class MpesaConfig:
    CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY", "sandbox_key")
    CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET", "sandbox_secret")
    PASSKEY = os.getenv(
        "MPESA_PASSKEY",
        "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    )
    SHORTCODE = os.getenv("MPESA_SHORTCODE", "174379")
    ENVIRONMENT = os.getenv("MPESA_ENVIRONMENT", "sandbox")
    CALLBACK_URL = os.getenv(
        "MPESA_CALLBACK_URL", "https://example.com/api/mpesa/callback"
    )

    @classmethod
    def get_base_url(cls):
        return (
            "https://sandbox.safaricom.co.ke"
            if cls.ENVIRONMENT == "sandbox"
            else "https://api.safaricom.co.ke"
        )