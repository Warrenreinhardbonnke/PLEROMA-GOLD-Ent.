import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.states.order_state import OrderState


def order_confirmation_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "check_check",
                            class_name="mx-auto h-24 w-24 text-green-500 mb-6",
                        ),
                        rx.el.h1(
                            "Thank you for your order!",
                            class_name="text-3xl font-extrabold text-[#8B4513] sm:text-4xl mb-4",
                        ),
                        rx.el.p(
                            "Your order has been placed successfully.",
                            class_name="text-lg text-gray-500 mb-2",
                        ),
                        rx.el.p(
                            f"Order Number: #{OrderState.current_order['id']}",
                            class_name="text-xl font-semibold text-gray-900 mb-8",
                        ),
                        rx.cond(
                            OrderState.current_order["payment_method"]
                            == "Manual M-Pesa",
                            rx.el.div(
                                rx.el.h3(
                                    "Action Required: Complete Payment",
                                    class_name="text-lg font-bold text-[#8B4513] mb-4",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "To complete your order, please send the payment to:",
                                        class_name="text-gray-600 mb-3",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.span(
                                                "M-Pesa Number:",
                                                class_name="text-gray-500",
                                            ),
                                            rx.el.span(
                                                "0794807479",
                                                class_name="font-bold text-gray-900",
                                            ),
                                            class_name="flex justify-between mb-2",
                                        ),
                                        rx.el.div(
                                            rx.el.span(
                                                "Account Name:",
                                                class_name="text-gray-500",
                                            ),
                                            rx.el.span(
                                                "Catherine Moraa",
                                                class_name="font-bold text-gray-900",
                                            ),
                                            class_name="flex justify-between mb-2",
                                        ),
                                        rx.el.div(
                                            rx.el.span(
                                                "Amount:", class_name="text-gray-500"
                                            ),
                                            rx.el.span(
                                                f"KES {OrderState.current_order['total']}",
                                                class_name="font-bold text-[#8B4513]",
                                            ),
                                            class_name="flex justify-between mb-2",
                                        ),
                                        rx.el.div(
                                            rx.el.span(
                                                "Reference:", class_name="text-gray-500"
                                            ),
                                            rx.el.span(
                                                OrderState.current_order["id"],
                                                class_name="font-mono font-bold text-gray-900 bg-gray-100 px-2 py-1 rounded",
                                            ),
                                            class_name="flex justify-between items-center",
                                        ),
                                        class_name="bg-gray-50 p-4 rounded-lg border border-gray-200 mb-6 text-left max-w-sm mx-auto",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "After payment, please share the confirmation message or screenshot to WhatsApp for faster processing:",
                                            class_name="text-sm text-gray-600 mb-3",
                                        ),
                                        rx.el.a(
                                            rx.icon(
                                                "message-circle",
                                                class_name="w-5 h-5 mr-2",
                                            ),
                                            "Confirm via WhatsApp",
                                            href=f"https://wa.me/254794807479?text=I have paid for order {OrderState.current_order['id']}",
                                            class_name="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-[#25D366] hover:bg-[#128C7E] shadow-lg w-full sm:w-auto",
                                        ),
                                        class_name="text-center",
                                    ),
                                    class_name="mb-8",
                                ),
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "We've sent a confirmation email to your inbox. We'll notify you when your order ships.",
                                    class_name="text-gray-500 mb-8 max-w-md mx-auto",
                                )
                            ),
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Track Order",
                                href=f"/track-order/{OrderState.current_order['id']}",
                                class_name="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-[#8B4513] bg-[#F5DEB3] hover:bg-[#e3cba3] mr-4",
                            ),
                            rx.el.a(
                                "Continue Shopping",
                                href="/products",
                                class_name="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f]",
                            ),
                            class_name="flex justify-center",
                        ),
                    ),
                    class_name="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-24 text-center",
                )
            ),
            class_name="flex-grow bg-white",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )