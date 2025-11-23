import logging
from fastapi import Request
from app.database.service import DatabaseService


async def mpesa_callback(request: Request):
    try:
        data = await request.json()
        logging.info(f"M-Pesa Callback Received: {data}")
        body = data.get("Body", {}).get("stkCallback", {})
        result_code = body.get("ResultCode")
        checkout_request_id = body.get("CheckoutRequestID")
        if result_code == 0:
            meta = body.get("CallbackMetadata", {}).get("Item", [])
            receipt_number = next(
                (
                    item.get("Value")
                    for item in meta
                    if item.get("Name") == "MpesaReceiptNumber"
                ),
                None,
            )
            if checkout_request_id:
                DatabaseService.update_order_by_checkout_id(
                    checkout_request_id,
                    {
                        "status": "Processing",
                        "payment_method": "M-Pesa",
                        "mpesa_receipt_number": receipt_number,
                    },
                )
                logging.info(
                    f"Order updated for CheckoutRequestID: {checkout_request_id}"
                )
        elif checkout_request_id:
            DatabaseService.update_order_by_checkout_id(
                checkout_request_id, {"status": "Payment Failed"}
            )
            logging.warning(
                f"Payment failed for CheckoutRequestID: {checkout_request_id}"
            )
        return {"ResultCode": 0, "ResultDesc": "Accepted"}
    except Exception as e:
        logging.exception(f"Error processing M-Pesa callback: {e}")
        return {"ResultCode": 1, "ResultDesc": "Internal Error"}