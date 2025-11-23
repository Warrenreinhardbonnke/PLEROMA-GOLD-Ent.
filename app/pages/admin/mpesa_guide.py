import reflex as rx
from app.components.admin_sidebar import admin_layout

GUIDE_CONTENT = """
# PLEROMA GOLD - M-PESA INTEGRATION & SETUP GUIDE

This guide provides a comprehensive walkthrough for configuring, testing, and going live with the M-Pesa payment integration.

## 1. Where Does the Money Go?

When a customer makes a payment via the Pleroma Gold app, the funds are settled directly into your **Safaricom Business M-Pesa Account**.

*   **Paybill**: Money goes to your designated Paybill account (e.g., 888888).
*   **Till Number (Buy Goods)**: Money goes to your store's Till Number.
*   **Settlement**: Funds accumulate in your M-Pesa portal (https://org.safaricom.co.ke/). You can withdraw these funds to your bank account or to a nominated personal M-Pesa number.

**Note**: The Pleroma Gold app does *not* hold any funds. It simply instructs Safaricom to initiate a transaction from the customer's phone to your business account.

## 2. Getting M-Pesa Credentials

To connect the app to M-Pesa, you need an API account on the Safaricom Daraja Portal.

### Step-by-Step:
1.  **Register/Login**: Go to [Safaricom Daraja Portal](https://developer.safaricom.co.ke/) and create an account.
2.  **Create a New App**:
    *   Go to **My Apps** > **Create a New App**.
    *   Give it a name (e.g., "PleromaGoldProd").
    *   Check the box for **Lipa na M-Pesa Sandbox** (for testing) or **Lipa na M-Pesa Production** (for live).
    *   Ensure `Mpesa Express` (STK Push) is selected.
3.  **Get Keys**:
    *   Once created, click on the app name.
    *   You will see **Consumer Key** and **Consumer Secret**. Copy these.

## 3. Paybill vs. Till Number

The integration supports both, but they behave slightly differently.

| Feature | Paybill | Till Number (Buy Goods) |
| :--- | :--- | :--- |
| **Account Type** | Used for collecting payments with an account number. | Used for "Buy Goods" where no account number is needed. |
| **User Input** | User sees "Pay to [Business] Account [Order ID]". | User sees "Buy Goods at [Business]". |
| **Config** | `MPESA_ACCOUNT_TYPE="Paybill"` | `MPESA_ACCOUNT_TYPE="Till"` |
| **Identifier** | Uses the Paybill Number (Shortcode). | Uses the Till Number (Shortcode). |

**Recommendation**: Use **Paybill** if you want easier reconciliation of specific orders, as the Order ID matches the "Account Number" field in the payment.

## 4. Configuration Steps

You need to configure the application environment variables to match your Safaricom credentials.

### Required Information:
*   **Shortcode**: Your Paybill or Till Number (e.g., 174379 for Sandbox).
*   **Passkey**: A long string provided by Safaricom.
    *   *Sandbox*: Use the static sandbox passkey: `bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919`
    *   *Production*: Sent to your email after "Going Live" on Daraja.
*   **Callback URL**: The public URL where Safaricom sends payment notifications.
    *   Must be **HTTPS**.
    *   Format: `https://your-domain.com/api/mpesa/callback`

### Environment Variables (`.env` file):

env
# M-Pesa Configuration
MPESA_ENVIRONMENT="sandbox"  # or "production"
MPESA_CONSUMER_KEY="<Your Consumer Key>"
MPESA_CONSUMER_SECRET="<Your Consumer Secret>"
MPESA_SHORTCODE="174379"     # Replace with your Paybill/Till
MPESA_PASSKEY="<Your Passkey>"
MPESA_ACCOUNT_TYPE="Paybill" # or "Till"
MPESA_CALLBACK_URL="https://your-domain.com/api/mpesa/callback"


## 5. Going Live (Production)

To move from Sandbox (Testing) to Production (Real Money):

1.  **Go Live Request**: On the Daraja Portal, click "Go Live".
2.  **Verification**: Upload required documents (CR12, Director ID, etc.) to verify ownership of the Paybill/Till.
3.  **Production App**: Once verified, create a NEW App in Daraja selected for "Production".
4.  **Credentials**: Use the NEW Consumer Key/Secret from the Production App.
5.  **Passkey**: Check your email for the Production Passkey.
6.  **Update Config**: Update your `.env` file with the new production values and set `MPESA_ENVIRONMENT="production"`.

## 6. How to Test Payments

### Method A: Sandbox Simulator (Recommended for Dev)
1.  Use the Sandbox Credentials (Shortcode `174379`).
2.  Initiate a payment from the Pleroma Gold checkout page using any phone number.
3.  Go to the [Daraja Sandbox Simulator](https://developer.safaricom.co.ke/test_credentials).
4.  Simulate the payment to see the callback hit your app.

### Method C: Live Testing
1.  Configure `.env` with Production credentials.
2.  Set the item price to KES 1 (create a test product).
3.  Checkout using your real phone number.
4.  You should receive the STK Push on your phone.
5.  Enter PIN and pay.
6.  Verify the order status changes to "Processing" in the Pleroma Gold Admin Dashboard.

## 7. Verification & Troubleshooting

### How to verify payments are going to your account:
1.  **Admin Dashboard**: Check the Orders page. Status should auto-update to "Processing" or "Paid".
2.  **M-Pesa Portal**: Login to [https://org.safaricom.co.ke](https://org.safaricom.co.ke). Check "Transactions" or "Statements". You should see the funds credited immediately.
3.  **SMS**: You (the business owner) will receive an SMS from Safaricom confirming receipt of funds.
"""


def mpesa_guide_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.markdown(
                GUIDE_CONTENT,
                class_name="prose prose-slate max-w-none prose-headings:text-[#8B4513] prose-a:text-[#DAA520]",
            ),
            class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100",
        ),
        class_name="p-6 max-w-5xl mx-auto",
    )


def admin_mpesa_guide_page() -> rx.Component:
    return admin_layout(mpesa_guide_content())