import reflex as rx
from app.states.wishlist_state import WishlistState
from app.components.navbar import navbar
from app.components.footer import footer


def wishlist_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=item["image"],
                    alt=item["name"],
                    class_name="w-full h-48 object-cover rounded-t-lg",
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        item["name"],
                        class_name="text-lg font-semibold text-[#8B4513] truncate",
                    ),
                    rx.el.p(
                        item["category"],
                        class_name="text-sm text-[#DAA520] font-medium mb-2",
                    ),
                    rx.el.div(
                        rx.foreach(
                            [1, 2, 3, 4, 5],
                            lambda i: rx.cond(
                                i <= item["rating"].to(int),
                                rx.icon(
                                    "star",
                                    class_name="h-4 w-4 text-[#DAA520] fill-current",
                                ),
                                rx.icon("star", class_name="h-4 w-4 text-gray-300"),
                            ),
                        ),
                        class_name="flex items-center mb-3",
                    ),
                    rx.el.span(
                        f"KES {item['price']}",
                        class_name="text-xl font-bold text-gray-900 block mb-4",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Move to Cart",
                            on_click=lambda: WishlistState.move_to_cart(item),
                            class_name="flex-1 bg-[#8B4513] text-white px-4 py-2 rounded-md hover:bg-[#6d360f] transition-colors text-sm font-medium",
                        ),
                        rx.el.button(
                            rx.icon("trash-2", class_name="h-5 w-5"),
                            on_click=lambda: WishlistState.remove_from_wishlist(
                                item["id"]
                            ),
                            class_name="ml-2 p-2 text-red-500 hover:bg-red-50 rounded-md border border-gray-200",
                        ),
                        class_name="flex gap-2",
                    ),
                ),
                class_name="p-4",
            ),
            class_name="bg-white rounded-lg shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100",
        )
    )


def wishlist_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "My Wishlist",
                    class_name="text-3xl font-extrabold text-[#8B4513] mb-8",
                ),
                rx.cond(
                    WishlistState.items.length() > 0,
                    rx.el.div(
                        rx.foreach(WishlistState.items, wishlist_item),
                        class_name="grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-8",
                    ),
                    rx.el.div(
                        rx.icon(
                            "heart", class_name="h-16 w-16 text-gray-300 mx-auto mb-4"
                        ),
                        rx.el.h3(
                            "Your wishlist is empty",
                            class_name="text-lg font-medium text-gray-900",
                        ),
                        rx.el.p(
                            "Start saving your favorite natural products!",
                            class_name="text-gray-500 mt-2",
                        ),
                        rx.el.a(
                            "Explore Products",
                            href="/products",
                            class_name="mt-6 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f]",
                        ),
                        class_name="text-center py-20 bg-white rounded-lg border border-gray-200",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
            class_name="flex-grow bg-gray-50",
        ),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )