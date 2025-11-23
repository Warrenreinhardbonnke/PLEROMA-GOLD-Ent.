import reflex as rx
from app.states.cart_state import CartState
from app.components.navbar import navbar
from app.components.footer import footer


def cart_item(item: dict) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.image(
                src=item["image"],
                alt=item["name"],
                class_name="h-24 w-24 rounded-md object-cover object-center sm:h-32 sm:w-32",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            rx.el.a(
                                item["name"],
                                href=f"/product/{item['id']}",
                                class_name="font-medium text-gray-700 hover:text-[#8B4513]",
                            ),
                            class_name="text-base",
                        ),
                        rx.el.p(
                            item["category"], class_name="mt-1 text-sm text-gray-500"
                        ),
                        rx.el.p(
                            f"KES {item['price']}",
                            class_name="mt-1 text-sm font-medium text-gray-900",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.button(
                                rx.icon("minus", class_name="h-4 w-4"),
                                on_click=lambda: CartState.decrement_quantity(
                                    item["id"]
                                ),
                                class_name="p-1 rounded-md text-gray-400 hover:text-gray-500",
                            ),
                            rx.el.span(
                                item["quantity"],
                                class_name="mx-2 text-gray-700 font-medium",
                            ),
                            rx.el.button(
                                rx.icon("plus", class_name="h-4 w-4"),
                                on_click=lambda: CartState.increment_quantity(
                                    item["id"]
                                ),
                                class_name="p-1 rounded-md text-gray-400 hover:text-gray-500",
                            ),
                            class_name="flex items-center border border-gray-200 rounded-md",
                        ),
                        rx.el.button(
                            rx.icon("trash-2", class_name="h-5 w-5"),
                            on_click=lambda: CartState.remove_from_cart(item["id"]),
                            class_name="ml-4 text-sm font-medium text-red-500 hover:text-red-600",
                        ),
                        class_name="flex items-end justify-between text-sm ml-4",
                    ),
                    class_name="flex justify-between sm:grid sm:grid-cols-2 sm:gap-x-6",
                ),
                class_name="relative flex flex-1 flex-col justify-between sm:ml-6",
            ),
            class_name="flex py-6 sm:py-10",
        ),
        class_name="border-b border-gray-200",
    )


def cart_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Shopping Cart",
                    class_name="text-3xl font-extrabold tracking-tight text-[#8B4513] sm:text-4xl",
                ),
                rx.cond(
                    CartState.items.length() > 0,
                    rx.el.div(
                        rx.el.div(
                            rx.el.ul(
                                rx.foreach(CartState.items, cart_item),
                                class_name="divide-y divide-gray-200",
                            ),
                            class_name="mt-12 lg:grid lg:grid-cols-12 lg:gap-x-12 lg:items-start",
                        ),
                        rx.el.section(
                            rx.el.h2(
                                "Order Summary",
                                class_name="text-lg font-medium text-gray-900",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.dt(
                                        "Subtotal", class_name="text-sm text-gray-600"
                                    ),
                                    rx.el.dd(
                                        f"KES {CartState.subtotal}",
                                        class_name="text-sm font-medium text-gray-900",
                                    ),
                                    class_name="flex items-center justify-between border-b border-gray-200 py-4",
                                ),
                                rx.el.div(
                                    rx.el.dt(
                                        "Discount", class_name="text-sm text-gray-600"
                                    ),
                                    rx.el.dd(
                                        f"- KES {CartState.discount_amount}",
                                        class_name="text-sm font-medium text-green-600",
                                    ),
                                    class_name="flex items-center justify-between border-b border-gray-200 py-4",
                                ),
                                rx.el.div(
                                    rx.el.dt(
                                        "Total",
                                        class_name="text-base font-medium text-gray-900",
                                    ),
                                    rx.el.dd(
                                        f"KES {CartState.total_price}",
                                        class_name="text-base font-medium text-[#8B4513]",
                                    ),
                                    class_name="flex items-center justify-between py-4",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.input(
                                            placeholder="Promo Code",
                                            on_change=CartState.set_discount_code,
                                            class_name="block w-full border-gray-300 rounded-md shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm px-4 py-2 border",
                                        ),
                                        rx.el.button(
                                            "Apply",
                                            on_click=CartState.apply_discount,
                                            class_name="ml-4 bg-[#F5DEB3] border border-transparent rounded-md shadow-sm py-2 px-4 text-sm font-medium text-[#8B4513] hover:bg-[#e3cba3] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#DAA520]",
                                        ),
                                        class_name="flex items-center mt-4",
                                    ),
                                    class_name="border-t border-gray-200 pt-4",
                                ),
                                rx.el.div(
                                    rx.el.a(
                                        "Proceed to Checkout",
                                        href="/checkout",
                                        class_name="w-full bg-[#8B4513] border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513] flex justify-center mt-6",
                                    )
                                ),
                                class_name="mt-4 bg-gray-50 rounded-lg px-4 py-6 sm:p-6 lg:p-8",
                            ),
                            class_name="mt-16 lg:mt-0 lg:col-span-5",
                        ),
                        class_name="lg:grid lg:grid-cols-12 lg:gap-x-12 lg:items-start mt-12",
                    ),
                    rx.el.div(
                        rx.icon(
                            "shopping-cart",
                            class_name="mx-auto h-12 w-12 text-gray-400",
                        ),
                        rx.el.h3(
                            "Your cart is empty",
                            class_name="mt-2 text-sm font-medium text-gray-900",
                        ),
                        rx.el.p(
                            "Start adding some delicious natural products!",
                            class_name="mt-1 text-sm text-gray-500",
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Start Shopping",
                                href="/products",
                                class_name="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513]",
                            ),
                            class_name="mt-6",
                        ),
                        class_name="text-center py-24 bg-white rounded-lg border-2 border-dashed border-gray-300 mt-12",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 bg-white",
            ),
            class_name="flex-grow bg-white",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )