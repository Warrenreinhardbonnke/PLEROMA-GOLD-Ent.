import reflex as rx
from app.states.product_state import ProductState
from app.components.product_card import product_card
from app.components.navbar import navbar
from app.components.footer import footer


def filter_tab(category: str) -> rx.Component:
    is_selected = ProductState.selected_category == category
    return rx.el.button(
        category,
        on_click=lambda: ProductState.set_category(category),
        class_name=rx.cond(
            is_selected,
            "px-6 py-2 bg-[#FFB800] text-black text-sm font-bold tracking-wider transition-all shadow-[0_0_15px_rgba(255,184,0,0.4)] clip-path-polygon-[10%_0,100%_0,90%_100%,0_100%]",
            "px-6 py-2 bg-transparent text-gray-400 border border-white/20 text-sm font-medium hover:border-[#FFB800] hover:text-[#FFB800] transition-all clip-path-polygon-[10%_0,100%_0,90%_100%,0_100%]",
        ),
    )


def products_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "SYSTEM INVENTORY",
                        class_name="text-4xl font-bold text-white sm:text-5xl font-['Rajdhani'] drop-shadow-[0_0_10px_#FFB800]",
                    ),
                    rx.el.p(
                        "Browse our quantum-enhanced selection of natural energy sources.",
                        class_name="mt-4 text-xl text-gray-400 font-light",
                    ),
                    class_name="text-center py-16 bg-gradient-to-b from-[#0F0F12] to-[#050505] border-b border-white/5",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.foreach(ProductState.categories, filter_tab),
                            class_name="flex flex-wrap gap-4 justify-center mb-8 md:mb-0 md:justify-start",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "search",
                                    class_name="absolute left-3 top-2.5 h-5 w-5 text-gray-500",
                                ),
                                rx.el.input(
                                    placeholder="Search database...",
                                    on_change=ProductState.set_search_query.debounce(
                                        300
                                    ),
                                    class_name="pl-10 pr-4 py-2 bg-[#0A0A0C] border border-white/10 rounded-none focus:ring-1 focus:ring-[#FFB800] focus:border-[#FFB800] text-gray-300 placeholder-gray-600 w-full md:w-64 transition-all",
                                ),
                                class_name="relative mb-4 md:mb-0",
                            ),
                            rx.el.div(
                                rx.el.select(
                                    rx.el.option("Popularity", value="Popularity"),
                                    rx.el.option(
                                        "Price: Low to High", value="Price: Low to High"
                                    ),
                                    rx.el.option(
                                        "Price: High to Low", value="Price: High to Low"
                                    ),
                                    rx.el.option("Newest", value="Newest"),
                                    on_change=ProductState.set_sort_option,
                                    class_name="block w-full pl-3 pr-10 py-2 text-base bg-[#0A0A0C] border border-white/10 text-gray-300 focus:outline-none focus:ring-1 focus:ring-[#FFB800] focus:border-[#FFB800] sm:text-sm rounded-none",
                                ),
                                class_name="w-full md:w-48",
                            ),
                            class_name="flex flex-col md:flex-row gap-4 w-full md:w-auto",
                        ),
                        class_name="flex flex-col md:flex-row justify-between items-center mb-12 space-y-6 md:space-y-0 pt-8",
                    ),
                    rx.el.div(
                        rx.cond(
                            ProductState.filtered_products.length() > 0,
                            rx.el.div(
                                rx.foreach(
                                    ProductState.filtered_products, product_card
                                ),
                                class_name="grid grid-cols-1 gap-y-12 gap-x-8 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:gap-x-10",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        "search-x",
                                        class_name="h-16 w-16 text-gray-600 mx-auto mb-4",
                                    ),
                                    rx.el.h3(
                                        "No data found",
                                        class_name="text-lg font-bold text-white",
                                    ),
                                    rx.el.p(
                                        "Recalibrate your search parameters.",
                                        class_name="text-gray-500 mt-2",
                                    ),
                                    class_name="text-center py-20 bg-[#0A0A0C] border border-white/5",
                                ),
                                class_name="w-full",
                            ),
                        )
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
                ),
            ),
            class_name="flex-grow bg-[#050505]",
        ),
        footer(),
        class_name="font-['Rajdhani'] bg-[#050505] min-h-screen flex flex-col",
    )