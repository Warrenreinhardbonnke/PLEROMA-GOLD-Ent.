import requests
import base64
import logging
from datetime import datetime
from typing import Optional
from app.config.mpesa_config import MpesaConfig


class MpesaService:
    _access_token: Optional[str] = None
    _token_expiry: float = 0

    @classmethod
    def get_access_token(cls) -> Optional[str]:
        if cls._access_token and datetime.now().timestamp() < cls._token_expiry:
            return cls._access_token
        url = f"{MpesaConfig.get_base_url()}/oauth/v1/generate?grant_type=client_credentials"
        try:
            auth = base64.b64encode(
                f"{MpesaConfig.CONSUMER_KEY}:{MpesaConfig.CONSUMER_SECRET}".encode()
            ).decode()
            headers = {"Authorization": f"Basic {auth}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            cls._access_token = data["access_token"]
            cls._token_expiry = (
                datetime.now().timestamp() + int(data["expires_in"]) - 60
            )
            return cls._access_token
        except Exception as e:
            logging.exception(f"Failed to get M-Pesa access token: {e}")
            return None

    @classmethod
    def get_password(cls) -> tuple[str, str]:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password_str = f"{MpesaConfig.SHORTCODE}{MpesaConfig.PASSKEY}{timestamp}"
        encoded_password = base64.b64encode(password_str.encode()).decode()
        return (encoded_password, timestamp)

    @classmethod
    def initiate_stk_push(
        cls, phone: str, amount: int, order_id: str
    ) -> Optional[dict]:
        token = cls.get_access_token()
        if not token:
            return None
        password, timestamp = cls.get_password()
        formatted_phone = phone
        if phone.startswith("0"):
            formatted_phone = "254" + phone[1:]
        elif phone.startswith("+"):
            formatted_phone = phone[1:]
        payload = {
            "BusinessShortCode": MpesaConfig.SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": formatted_phone,
            "PartyB": MpesaConfig.SHORTCODE,
            "PhoneNumber": formatted_phone,
            "CallBackURL": MpesaConfig.CALLBACK_URL,
            "AccountReference": order_id,
            "TransactionDesc": f"Payment for Order {order_id}",
        }
        url = f"{MpesaConfig.get_base_url()}/mpesa/stkpush/v1/processrequest"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.exception(f"M-Pesa STK Push failed: {e}")
            if hasattr(e, "response") and e.response is not None:
                logging.error(f"M-Pesa Error Response: {e.response.text}")
            return None

    @classmethod
    def query_transaction_status(cls, checkout_request_id: str) -> Optional[dict]:
        token = cls.get_access_token()
        if not token:
            return None
        password, timestamp = cls.get_password()
        payload = {
            "BusinessShortCode": MpesaConfig.SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "CheckoutRequestID": checkout_request_id,
        }
        url = f"{MpesaConfig.get_base_url()}/mpesa/stkpushquery/v1/query"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.exception(f"M-Pesa Query failed: {e}")
            return None