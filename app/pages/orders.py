import reflex as rx
from app.states.order_state import OrderState
from app.components.navbar import navbar
from app.components.footer import footer


def order_status_badge(status: str) -> rx.Component:
    return rx.match(
        status,
        (
            "Delivered",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800",
            ),
        ),
        (
            "Processing",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800",
            ),
        ),
        (
            "Pending",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800",
            ),
        ),
        (
            "Cancelled",
            rx.el.span(
                status,
                class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800",
            ),
        ),
        rx.el.span(
            status,
            class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800",
        ),
    )


def order_card(order: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        f"Order #{order['id']}",
                        class_name="text-lg leading-6 font-medium text-gray-900",
                    ),
                    rx.el.p(
                        f"Placed on {order['date']}",
                        class_name="mt-1 text-sm text-gray-500",
                    ),
                ),
                order_status_badge(order["status"]),
                class_name="flex items-center justify-between",
            ),
            rx.el.div(
                rx.foreach(
                    order["items"],
                    lambda item: rx.el.div(
                        rx.image(
                            src=item["image"],
                            class_name="h-16 w-16 object-cover rounded-md border border-gray-200",
                        ),
                        rx.el.div(
                            rx.el.h4(
                                item["name"],
                                class_name="text-sm font-medium text-gray-900",
                            ),
                            rx.el.p(
                                f"Qty: {item['quantity']}",
                                class_name="text-sm text-gray-500",
                            ),
                            class_name="ml-4",
                        ),
                        class_name="flex items-center mb-4 last:mb-0",
                    ),
                ),
                class_name="mt-6 border-t border-gray-200 pt-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Total Amount:", class_name="text-sm font-medium text-gray-500"
                    ),
                    rx.el.span(
                        f"KES {order['total']}",
                        class_name="ml-2 text-lg font-bold text-[#8B4513]",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.div(
                    rx.el.a(
                        "Track Order",
                        href=f"/track-order/{order['id']}",
                        class_name="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none",
                    ),
                    rx.el.a(
                        "View Details",
                        href="#",
                        class_name="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f] shadow-sm",
                    ),
                    class_name="flex",
                ),
                class_name="mt-6 flex items-center justify-between border-t border-gray-200 pt-6",
            ),
            class_name="px-4 py-5 sm:p-6",
        ),
        class_name="bg-white overflow-hidden shadow rounded-lg border border-gray-200 mb-6",
    )


def filter_tab(name: str) -> rx.Component:
    is_selected = OrderState.selected_filter == name
    return rx.el.button(
        name,
        on_click=lambda: OrderState.set_filter(name),
        class_name=rx.cond(
            is_selected,
            "px-4 py-2 rounded-full bg-[#8B4513] text-white text-sm font-medium transition-all shadow-md",
            "px-4 py-2 rounded-full bg-white text-gray-600 border border-gray-200 text-sm font-medium hover:bg-gray-50 transition-all",
        ),
    )


def orders_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "My Orders",
                        class_name="text-3xl font-extrabold text-[#8B4513] mb-8",
                    ),
                    rx.el.div(
                        rx.foreach(
                            [
                                "All Orders",
                                "Pending",
                                "Processing",
                                "Delivered",
                                "Cancelled",
                            ],
                            filter_tab,
                        ),
                        class_name="flex flex-wrap gap-2 mb-8",
                    ),
                    rx.cond(
                        OrderState.filtered_orders.length() > 0,
                        rx.el.div(rx.foreach(OrderState.filtered_orders, order_card)),
                        rx.el.div(
                            rx.icon(
                                "shopping-bag",
                                class_name="h-16 w-16 text-gray-300 mx-auto mb-4",
                            ),
                            rx.el.h3(
                                "No orders found",
                                class_name="text-lg font-medium text-gray-900",
                            ),
                            rx.el.p(
                                "You haven't placed any orders yet.",
                                class_name="text-gray-500 mt-2",
                            ),
                            rx.el.a(
                                "Start Shopping",
                                href="/products",
                                class_name="mt-6 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f]",
                            ),
                            class_name="text-center py-20 bg-white rounded-lg border border-gray-200",
                        ),
                    ),
                ),
                class_name="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
            class_name="flex-grow bg-gray-50",
        ),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )