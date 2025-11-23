import reflex as rx
from app.components.admin_sidebar import admin_layout
from app.states.admin_order_state import AdminOrderState


def order_row(order: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(order["id"], class_name="text-sm font-medium text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(order["customer"], class_name="text-sm text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(order["date"], class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(f"{order['items']} items", class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                f"KES {order['total']}", class_name="text-sm font-medium text-[#8B4513]"
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    order["payment_method"],
                    class_name="text-sm font-medium text-gray-900",
                ),
                rx.cond(
                    order["receipt_number"] != "-",
                    rx.el.div(
                        order["receipt_number"],
                        class_name="text-xs text-gray-500 font-mono",
                    ),
                ),
                class_name="flex flex-col",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.match(
                order["status"],
                (
                    "Paid",
                    rx.el.span(
                        "Paid",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800",
                    ),
                ),
                (
                    "Delivered",
                    rx.el.span(
                        "Delivered",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800 border border-gray-200",
                    ),
                ),
                (
                    "Processing",
                    rx.el.span(
                        "Processing",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800",
                    ),
                ),
                (
                    "Pending",
                    rx.el.span(
                        "Pending",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800",
                    ),
                ),
                (
                    "Cancelled",
                    rx.el.span(
                        "Cancelled",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800",
                    ),
                ),
                rx.el.span(
                    order["status"],
                    class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.select(
                rx.el.option("Paid", value="Paid"),
                rx.el.option("Pending", value="Pending"),
                rx.el.option("Processing", value="Processing"),
                rx.el.option("Delivered", value="Delivered"),
                rx.el.option("Cancelled", value="Cancelled"),
                value=order["status"],
                on_change=lambda v: AdminOrderState.update_status(order["id"], v),
                class_name="block w-full pl-3 pr-8 py-1 text-xs border-gray-300 focus:outline-none focus:ring-[#DAA520] focus:border-[#DAA520] rounded-md",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium",
        ),
    )


def orders_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Order Management", class_name="text-2xl font-bold text-gray-900 mb-6"
            )
        ),
        rx.el.div(
            rx.foreach(
                AdminOrderState.status_options,
                lambda s: rx.el.button(
                    s,
                    on_click=lambda: AdminOrderState.set_filter(s),
                    class_name=rx.cond(
                        AdminOrderState.filter_status == s,
                        "px-3 py-1 rounded-full bg-[#8B4513] text-white text-sm font-medium",
                        "px-3 py-1 rounded-full bg-white border border-gray-300 text-gray-600 text-sm font-medium hover:bg-gray-50",
                    ),
                ),
            ),
            class_name="flex flex-wrap gap-2 mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Order ID",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Customer",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Items",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Total",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Payment",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Action",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50",
                ),
                rx.el.tbody(
                    rx.foreach(AdminOrderState.filtered_orders, order_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg overflow-x-auto",
        ),
        class_name="p-6 max-w-7xl mx-auto",
    )


def admin_orders_page() -> rx.Component:
    return admin_layout(orders_content())