import reflex as rx
from app.states.order_state import OrderState
from app.components.navbar import navbar
from app.components.footer import footer


def tracking_step(
    title: str, date: str, is_completed: bool, is_current: bool
) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.cond(
                is_completed,
                rx.el.span(
                    rx.icon("check", class_name="h-5 w-5 text-white"),
                    class_name="flex h-8 w-8 items-center justify-center rounded-full bg-[#8B4513] ring-8 ring-white",
                ),
                rx.cond(
                    is_current,
                    rx.el.span(
                        rx.el.span(
                            class_name="h-2.5 w-2.5 rounded-full bg-[#8B4513] animate-pulse"
                        ),
                        class_name="flex h-8 w-8 items-center justify-center rounded-full bg-[#DAA520] ring-8 ring-white",
                    ),
                    rx.el.span(
                        class_name="flex h-8 w-8 items-center justify-center rounded-full bg-gray-200 ring-8 ring-white"
                    ),
                ),
            ),
            class_name="absolute left-0 top-4 -ml-px h-full w-0.5 bg-gray-200",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(title, class_name="font-medium text-gray-900"),
                rx.el.p(date, class_name="text-sm text-gray-500"),
                class_name="flex flex-col",
            ),
            class_name="ml-12 pb-12",
        ),
        class_name="relative pb-10",
    )


def order_tracking_page() -> rx.Component:
    order = OrderState.current_order
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.a(
                            rx.icon("arrow-left", class_name="h-5 w-5 mr-2"),
                            "Back to Orders",
                            href="/orders",
                            class_name="flex items-center text-sm text-gray-500 hover:text-[#8B4513] mb-6",
                        ),
                        rx.el.h1(
                            f"Track Order #{order['id']}",
                            class_name="text-3xl font-extrabold text-[#8B4513]",
                        ),
                        rx.el.p(
                            f"Placed on {order['date']}",
                            class_name="mt-2 text-gray-500",
                        ),
                        class_name="mb-12",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h2(
                                "Order Status",
                                class_name="text-lg font-medium text-gray-900 mb-6",
                            ),
                            rx.el.nav(
                                rx.el.ol(
                                    tracking_step(
                                        "Order Placed", "Oct 24, 2023", True, False
                                    ),
                                    tracking_step(
                                        "Processing", "Oct 25, 2023", True, False
                                    ),
                                    tracking_step(
                                        "Shipped", "Oct 26, 2023", True, False
                                    ),
                                    tracking_step(
                                        "Out for Delivery", "Oct 27, 2023", True, False
                                    ),
                                    tracking_step(
                                        "Delivered", "Oct 28, 2023", True, True
                                    ),
                                    class_name="overflow-hidden",
                                ),
                                class_name="relative",
                            ),
                            class_name="bg-white p-8 shadow rounded-lg border border-gray-200 mb-8",
                        ),
                        rx.el.div(
                            rx.el.h2(
                                "Shipping Details",
                                class_name="text-lg font-medium text-gray-900 mb-6",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h3(
                                        "Shipping Address",
                                        class_name="font-medium text-gray-900",
                                    ),
                                    rx.el.p(
                                        "John Doe", class_name="mt-2 text-gray-500"
                                    ),
                                    rx.el.p(
                                        "123 Street Name", class_name="text-gray-500"
                                    ),
                                    rx.el.p(
                                        "Nairobi, 00100", class_name="text-gray-500"
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.h3(
                                        "Estimated Delivery",
                                        class_name="font-medium text-gray-900",
                                    ),
                                    rx.el.p(
                                        "Oct 28, 2023",
                                        class_name="mt-2 text-[#8B4513] font-semibold",
                                    ),
                                ),
                                class_name="bg-white p-8 shadow rounded-lg border border-gray-200",
                            ),
                            class_name="h-full",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-8",
                    ),
                ),
                class_name="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
            class_name="flex-grow bg-gray-50",
        ),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )