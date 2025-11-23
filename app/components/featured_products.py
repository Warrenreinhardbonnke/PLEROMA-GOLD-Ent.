import reflex as rx
from app.states.product_state import ProductState
from app.components.product_card import product_card


def featured_products() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "FEATURED INVENTORY",
                    class_name="text-3xl font-bold tracking-[0.1em] text-white sm:text-4xl text-center mb-16 font-['Rajdhani'] drop-shadow-[0_0_10px_#FFB800]",
                ),
                rx.el.div(
                    rx.foreach(ProductState.featured_products, product_card),
                    class_name="grid grid-cols-1 gap-y-12 gap-x-8 sm:grid-cols-2 lg:grid-cols-3 xl:gap-x-10",
                ),
                rx.el.div(
                    rx.el.a(
                        "ACCESS FULL CATALOG",
                        href="/products",
                        class_name="inline-flex items-center justify-center px-10 py-4 border border-[#FFB800] text-base font-bold tracking-widest rounded-none text-[#FFB800] bg-transparent hover:bg-[#FFB800] hover:text-black md:text-lg transition-all duration-300 shadow-[0_0_15px_rgba(255,184,0,0.2)] hover:shadow-[0_0_30px_rgba(255,184,0,0.6)]",
                    ),
                    class_name="mt-20 flex justify-center",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-24 bg-[#050505] bg-[linear-gradient(rgba(255,184,0,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,184,0,0.03)_1px,transparent_1px)] bg-[size:40px_40px]",
        ),
        id="products",
    )