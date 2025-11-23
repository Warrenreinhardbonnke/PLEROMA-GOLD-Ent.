import reflex as rx
from app.components.admin_sidebar import admin_layout
from app.states.admin_customer_state import AdminCustomerState


def customer_row(customer: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    customer["name"], class_name="text-sm font-medium text-gray-900"
                ),
                rx.el.div(customer["email"], class_name="text-sm text-gray-500"),
                class_name="flex flex-col",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(customer["phone"], class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(customer["total_orders"], class_name="text-sm text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                f"KES {customer['total_spent']:,}",
                class_name="text-sm font-medium text-green-600",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(customer["join_date"], class_name="text-sm text-gray-500"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.button(
                "View History",
                class_name="text-[#8B4513] hover:text-[#6d360f] text-sm font-medium",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
    )


def customers_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Customers", class_name="text-2xl font-bold text-gray-900 mb-6")
        ),
        rx.el.div(
            rx.icon(
                "search", class_name="absolute left-3 top-2.5 h-5 w-5 text-gray-400"
            ),
            rx.el.input(
                placeholder="Search customers...",
                on_change=AdminCustomerState.set_search_query,
                class_name="pl-10 block w-full md:w-64 border-gray-300 rounded-md shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm py-2 border",
            ),
            class_name="relative mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Customer",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Phone",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Orders",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Total Spent",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Joined",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    ),
                    class_name="bg-gray-50",
                ),
                rx.el.tbody(
                    rx.foreach(AdminCustomerState.filtered_customers, customer_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg overflow-x-auto",
        ),
        class_name="p-6 max-w-7xl mx-auto",
    )


def admin_customers_page() -> rx.Component:
    return admin_layout(customers_content())