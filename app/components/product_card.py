import reflex as rx
from app.states.cart_state import CartState


def product_card(product: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.image(
                        src=product["image"],
                        alt=product["name"],
                        class_name="w-full h-56 object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-500",
                    ),
                    rx.el.div(
                        class_name="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-60"
                    ),
                    href=f"/product/{product['id']}",
                    class_name="block relative overflow-hidden",
                ),
                class_name="relative clip-path-polygon-[0_0,100%_0,100%_85%,85%_100%,0_100%]",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        product["category"],
                        class_name="text-xs text-[#FFB800] font-mono tracking-widest mb-1 uppercase",
                    ),
                    rx.el.a(
                        rx.el.h3(
                            product["name"],
                            class_name="text-lg font-bold text-white truncate group-hover:text-[#FFB800] transition-colors font-['Rajdhani']",
                        ),
                        href=f"/product/{product['id']}",
                    ),
                ),
                rx.el.div(
                    rx.foreach(
                        [1, 2, 3, 4, 5],
                        lambda i: rx.cond(
                            i <= product["rating"].to(int),
                            rx.icon(
                                "star", class_name="h-3 w-3 text-[#FFB800] fill-current"
                            ),
                            rx.icon("star", class_name="h-3 w-3 text-gray-700"),
                        ),
                    ),
                    class_name="flex items-center mb-4 mt-2",
                ),
                rx.el.div(
                    rx.el.span(
                        f"KES {product['price']}",
                        class_name="text-xl font-bold text-[#FFB800] font-mono",
                    ),
                    rx.el.button(
                        rx.icon("plus", class_name="h-5 w-5"),
                        on_click=lambda: CartState.add_to_cart(product, 1),
                        class_name="flex items-center justify-center bg-[#FFB800]/10 hover:bg-[#FFB800] border border-[#FFB800] text-[#FFB800] hover:text-black h-10 w-10 rounded-none transition-all duration-300 shadow-[0_0_10px_rgba(255,184,0,0.1)] hover:shadow-[0_0_20px_rgba(255,184,0,0.5)]",
                    ),
                    class_name="flex items-center justify-between mt-4 border-t border-white/10 pt-4",
                ),
                class_name="p-5",
            ),
            class_name="group bg-[#0A0A0C] border border-white/5 hover:border-[#FFB800]/50 transition-all duration-500 h-full flex flex-col justify-between relative overflow-hidden hover:shadow-[0_0_30px_rgba(255,184,0,0.15)]",
        ),
        class_name="h-full",
    )