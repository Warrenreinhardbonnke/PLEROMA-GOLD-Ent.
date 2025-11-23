import reflex as rx
from app.states.product_state import ProductState
from app.states.cart_state import CartState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.product_card import product_card


def quantity_selector() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("minus", class_name="h-4 w-4"),
            on_click=ProductState.decrement_quantity,
            class_name="p-2 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 hover:bg-gray-100 text-gray-600",
        ),
        rx.el.div(
            ProductState.quantity,
            class_name="px-4 py-2 border-t border-b border-gray-300 text-center w-12 font-medium",
        ),
        rx.el.button(
            rx.icon("plus", class_name="h-4 w-4"),
            on_click=ProductState.increment_quantity,
            class_name="p-2 rounded-r-md border border-l-0 border-gray-300 bg-gray-50 hover:bg-gray-100 text-gray-600",
        ),
        class_name="flex items-center",
    )


def size_option(size: str) -> rx.Component:
    is_selected = ProductState.selected_size == size
    return rx.el.button(
        size,
        on_click=lambda: ProductState.set_size(size),
        class_name=rx.cond(
            is_selected,
            "px-4 py-2 border-2 border-[#8B4513] bg-[#F5DEB3]/20 text-[#8B4513] font-semibold rounded-md transition-all",
            "px-4 py-2 border border-gray-300 text-gray-600 hover:border-[#8B4513] rounded-md transition-all",
        ),
    )


def product_detail_content() -> rx.Component:
    p = ProductState.current_product
    return rx.el.div(
        rx.cond(
            p,
            rx.el.div(
                rx.el.nav(
                    rx.el.ol(
                        rx.el.li(
                            rx.el.a(
                                "Products",
                                href="/products",
                                class_name="hover:text-[#8B4513] transition-colors",
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.li(
                            rx.icon(
                                "chevron-right", class_name="h-4 w-4 mx-2 text-gray-400"
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.li(rx.el.span(p["category"], class_name="text-gray-500")),
                    ),
                    class_name="flex items-center text-sm text-gray-500 mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src=p["image"],
                            alt=p["name"],
                            class_name="w-full h-96 object-cover rounded-xl shadow-sm",
                        ),
                        class_name="space-y-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                p["category"],
                                class_name="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-[#F5DEB3] text-[#8B4513] mb-4",
                            ),
                            rx.el.h1(
                                p["name"],
                                class_name="text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl mb-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.foreach(
                                        [1, 2, 3, 4, 5],
                                        lambda i: rx.cond(
                                            i <= p["rating"].to(int),
                                            rx.icon(
                                                "star",
                                                class_name="h-5 w-5 text-[#DAA520] fill-current",
                                            ),
                                            rx.icon(
                                                "star",
                                                class_name="h-5 w-5 text-gray-300",
                                            ),
                                        ),
                                    ),
                                    class_name="flex items-center",
                                ),
                                rx.el.span(
                                    "(120 reviews)",
                                    class_name="ml-3 text-sm text-gray-500",
                                ),
                                class_name="flex items-center mb-6",
                            ),
                            rx.el.p(
                                p["description"],
                                class_name="text-base text-gray-700 mb-8 leading-relaxed",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    f"KES {p['price']}",
                                    class_name="text-3xl font-bold text-[#8B4513]",
                                ),
                                class_name="mb-8",
                            ),
                            rx.el.div(
                                rx.el.h3(
                                    "Select Size",
                                    class_name="text-sm font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    rx.foreach(ProductState.size_options, size_option),
                                    class_name="flex gap-3 mb-8",
                                ),
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h3(
                                        "Quantity",
                                        class_name="text-sm font-medium text-gray-900 mb-2",
                                    ),
                                    quantity_selector(),
                                    class_name="mr-8",
                                ),
                                rx.el.div(
                                    rx.el.button(
                                        "Add to Cart",
                                        on_click=lambda: CartState.add_to_cart(
                                            p, ProductState.quantity
                                        ),
                                        class_name="flex-1 bg-[#8B4513] border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513] shadow-lg hover:shadow-xl transition-all",
                                    ),
                                    class_name="flex-1",
                                ),
                                class_name="flex items-end gap-4 pt-8 border-t border-gray-200",
                            ),
                        )
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-x-12 gap-y-10",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Related Products",
                        class_name="text-2xl font-bold text-gray-900 mb-8",
                    ),
                    rx.el.div(
                        rx.foreach(ProductState.related_products, product_card),
                        class_name="grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8",
                    ),
                    class_name="mt-24 pt-12 border-t border-gray-200",
                ),
            ),
            rx.el.div(
                rx.el.h1(
                    "Product not found", class_name="text-2xl font-bold text-gray-900"
                ),
                rx.el.a(
                    "Back to Products",
                    href="/products",
                    class_name="text-[#8B4513] hover:underline mt-4 inline-block",
                ),
                class_name="text-center py-20",
            ),
        ),
        class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
    )


def product_detail_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(product_detail_content(), class_name="flex-grow bg-white"),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )