import reflex as rx
from app.components.admin_sidebar import admin_layout
from app.states.admin_product_state import AdminProductState


def product_row(product: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.image(
                    src=product["image"], class_name="h-10 w-10 rounded-md object-cover"
                ),
                rx.el.div(
                    rx.el.div(
                        product["name"], class_name="text-sm font-medium text-gray-900"
                    ),
                    rx.el.div(product["category"], class_name="text-sm text-gray-500"),
                    class_name="ml-4",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(f"KES {product['price']}", class_name="text-sm text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(product["stock"], class_name="text-sm text-gray-900"),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.match(
                product["status"],
                (
                    "In Stock",
                    rx.el.span(
                        "In Stock",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800",
                    ),
                ),
                (
                    "Low Stock",
                    rx.el.span(
                        "Low Stock",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800",
                    ),
                ),
                (
                    "Out of Stock",
                    rx.el.span(
                        "Out of Stock",
                        class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800",
                    ),
                ),
                rx.el.span(
                    product["status"],
                    class_name="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("share_2", class_name="h-4 w-4"),
                    class_name="text-blue-600 hover:text-blue-900 mr-3",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    on_click=lambda: AdminProductState.delete_product(product["id"]),
                    class_name="text-red-600 hover:text-red-900",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium",
        ),
    )


def products_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Products", class_name="text-2xl font-bold text-gray-900"),
            rx.el.button(
                rx.icon("plus", class_name="h-5 w-5 mr-2"),
                "Add Product",
                class_name="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f]",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.icon(
                "search", class_name="absolute left-3 top-2.5 h-5 w-5 text-gray-400"
            ),
            rx.el.input(
                placeholder="Search products...",
                on_change=AdminProductState.set_search_query,
                class_name="pl-10 block w-full md:w-64 border-gray-300 rounded-md shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm py-2 border",
            ),
            class_name="relative mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Product",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Price",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Stock",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
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
                    rx.foreach(AdminProductState.filtered_products, product_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg overflow-x-auto",
        ),
        class_name="p-6 max-w-7xl mx-auto",
    )


def admin_products_page() -> rx.Component:
    return admin_layout(products_content())