import os
import logging


class MpesaConfig:
    """
    Configuration settings for M-Pesa Daraja API integration.

    This class manages credentials and settings required to transact with Safaricom's M-Pesa API.
    It supports both 'Paybill' and 'Buy Goods (Till Number)' modes.

    FOR A COMPLETE SETUP GUIDE, REFER TO `MPESA_SETUP_GUIDE.md` IN THE ROOT DIRECTORY.
    """

    CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY", "sandbox_key").strip()
    CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET", "sandbox_secret").strip()
    _raw_shortcode = os.getenv("MPESA_SHORTCODE", "174379")
    SHORTCODE = _raw_shortcode.replace(" ", "").strip() if _raw_shortcode else ""
    PASSKEY = os.getenv(
        "MPESA_PASSKEY",
        "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    ).strip()
    ACCOUNT_TYPE = os.getenv("MPESA_ACCOUNT_TYPE", "Paybill").strip()
    ENVIRONMENT = os.getenv("MPESA_ENVIRONMENT", "sandbox").strip().lower()
    CALLBACK_URL = os.getenv(
        "MPESA_CALLBACK_URL", "https://example.com/api/mpesa/callback"
    ).strip()

    @classmethod
    def get_base_url(cls):
        """
        Returns the API base URL based on the environment setting.
        """
        return (
            "https://sandbox.safaricom.co.ke"
            if cls.ENVIRONMENT == "sandbox"
            else "https://api.safaricom.co.ke"
        )

    @classmethod
    def get_transaction_type(cls):
        """
        Returns the correct CommandID for the STK Push based on Account Type.
        """
        if cls.ACCOUNT_TYPE.lower() in ["till", "tillnumber", "buygoods"]:
            return "CustomerBuyGoodsOnline"
        return "CustomerPayBillOnline"

    @classmethod
    def validate(cls):
        """
        Validates that necessary configurations are present.
        Returns True if valid, False otherwise. Logs warnings for missing keys.
        """
        missing_configs = []
        if not cls.CONSUMER_KEY or cls.CONSUMER_KEY == "sandbox_key":
            if cls.ENVIRONMENT == "production":
                missing_configs.append("MPESA_CONSUMER_KEY")
        if not cls.CONSUMER_SECRET or cls.CONSUMER_SECRET == "sandbox_secret":
            if cls.ENVIRONMENT == "production":
                missing_configs.append("MPESA_CONSUMER_SECRET")
        if not cls.SHORTCODE:
            missing_configs.append("MPESA_SHORTCODE")
        if not cls.PASSKEY:
            missing_configs.append("MPESA_PASSKEY")
        if cls.PASSKEY and len(cls.PASSKEY) < 20 and (cls.ENVIRONMENT == "sandbox"):
            logging.warning(
                f"MPESA_PASSKEY seems unusually short ({len(cls.PASSKEY)} chars). Ensure it is the correct StkPush Passkey, not the portal password."
            )
        if missing_configs:
            error_msg = f"CRITICAL: Missing M-Pesa Configurations: {', '.join(missing_configs)}. Payments will fail. See MPESA_SETUP_GUIDE.md"
            logging.error(error_msg)
            return False
        return True