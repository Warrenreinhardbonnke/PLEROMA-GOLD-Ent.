import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


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
                            "Order Number: #PG-83920",
                            class_name="text-xl font-semibold text-gray-900 mb-8",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "We've sent a confirmation email to your inbox. We'll notify you when your order ships.",
                                class_name="text-gray-500 mb-8 max-w-md mx-auto",
                            )
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Track Order",
                                href="#",
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