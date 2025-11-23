import reflex as rx


def footer_link(text: str, url: str) -> rx.Component:
    return rx.el.li(
        rx.el.a(
            text,
            href=url,
            class_name="text-base text-gray-400 hover:text-[#FFB800] transition-all hover:translate-x-2 inline-block",
        )
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            class_name="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/hexellence.png')] opacity-5 pointer-events-none"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "PLEROMA GOLD",
                            class_name="text-lg font-bold text-[#FFB800] tracking-widest uppercase mb-2 font-['Rajdhani']",
                        ),
                        rx.el.p(
                            "Premium quality natural products for a healthier future. Sourced from the matrix of nature, delivered to your coordinate.",
                            class_name="mt-4 text-base text-gray-400 leading-relaxed",
                        ),
                        class_name="col-span-1 md:col-span-2 pr-8",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "NAVIGATION",
                            class_name="text-sm font-bold text-white tracking-widest uppercase mb-4",
                        ),
                        rx.el.ul(
                            footer_link("Home", "/"),
                            footer_link("Products", "#products"),
                            footer_link("About Us", "#about"),
                            footer_link("Contact", "#contact"),
                            class_name="space-y-3",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "TRANSMISSION",
                            class_name="text-sm font-bold text-white tracking-widest uppercase mb-4",
                        ),
                        rx.el.ul(
                            rx.el.li(
                                rx.el.div(
                                    rx.icon(
                                        "map-pin",
                                        class_name="h-5 w-5 text-[#FFB800] mr-3",
                                    ),
                                    rx.el.span(
                                        "Nairobi, Kenya", class_name="text-gray-400"
                                    ),
                                    class_name="flex items-center",
                                )
                            ),
                            rx.el.li(
                                rx.el.div(
                                    rx.icon(
                                        "phone",
                                        class_name="h-5 w-5 text-[#FFB800] mr-3",
                                    ),
                                    rx.el.span(
                                        "+254 700 000 000", class_name="text-gray-400"
                                    ),
                                    class_name="flex items-center",
                                )
                            ),
                            rx.el.li(
                                rx.el.div(
                                    rx.icon(
                                        "mail", class_name="h-5 w-5 text-[#FFB800] mr-3"
                                    ),
                                    rx.el.span(
                                        "info@pleromagold.co.ke",
                                        class_name="text-gray-400",
                                    ),
                                    class_name="flex items-center",
                                )
                            ),
                            class_name="space-y-4",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-4 gap-12",
                ),
                rx.el.div(
                    rx.el.p(
                        "© 2024 PLEROMA GOLD SYSTEMS. All rights reserved.",
                        class_name="text-sm text-gray-500 text-center font-mono",
                    ),
                    class_name="mt-16 border-t border-white/10 pt-8",
                ),
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8 relative z-10",
        ),
        class_name="bg-[#050505] border-t border-[#FFB800]/20 relative overflow-hidden",
        id="contact",
    )