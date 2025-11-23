import reflex as rx


def hero() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(255,184,0,0.15)_0%,rgba(0,0,0,0)_70%)] pointer-events-none z-0"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.main(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "FUTURE OF TASTE",
                                class_name="text-[#FFB800] font-mono text-sm tracking-[0.3em] mb-4 block",
                            )
                        ),
                        rx.el.h1(
                            rx.el.span(
                                "PREMIUM NATURAL ",
                                class_name="block xl:inline text-white drop-shadow-[0_0_10px_rgba(255,255,255,0.5)]",
                            ),
                            rx.el.span(
                                "NECTAR & NUTS",
                                class_name="block text-[#FFB800] xl:inline drop-shadow-[0_0_15px_rgba(255,184,0,0.8)]",
                            ),
                            class_name="text-5xl tracking-tight font-bold sm:text-6xl md:text-7xl font-['Rajdhani']",
                        ),
                        rx.el.p(
                            "Experience the quantum leap in flavor. 100% organic, molecularly perfected roasted groundnuts and pure natural honey. Sourced from the golden fields, delivered with precision.",
                            class_name="mt-6 text-base text-gray-300 sm:mt-8 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-8 md:text-xl lg:mx-0 font-light tracking-wide leading-relaxed border-l-2 border-[#FFB800] pl-6",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.a(
                                    "INITIATE ORDER",
                                    href="#products",
                                    class_name="w-full flex items-center justify-center px-8 py-4 border border-[#FFB800] text-base font-bold text-black bg-[#FFB800] hover:bg-[#FFA500] md:text-lg md:px-10 shadow-[0_0_20px_rgba(255,184,0,0.4)] hover:shadow-[0_0_30px_rgba(255,184,0,0.7)] transition-all duration-300 clip-path-polygon-[10%_0,100%_0,100%_70%,90%_100%,0_100%,0_30%]",
                                ),
                                class_name="rounded-md shadow",
                            ),
                            rx.el.div(
                                rx.el.a(
                                    "EXPLORE DATA",
                                    href="#about",
                                    class_name="w-full flex items-center justify-center px-8 py-4 border border-[#FFB800]/50 text-base font-bold text-[#FFB800] bg-transparent hover:bg-[#FFB800]/10 md:text-lg md:px-10 backdrop-blur-sm transition-all duration-300 clip-path-polygon-[10%_0,100%_0,100%_70%,90%_100%,0_100%,0_30%]",
                                ),
                                class_name="mt-3 sm:mt-0 sm:ml-6",
                            ),
                            class_name="mt-8 sm:mt-10 sm:flex sm:justify-center lg:justify-start",
                        ),
                        class_name="sm:text-center lg:text-left relative z-10",
                    ),
                    class_name="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28",
                ),
                class_name="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2 z-10",
            ),
            rx.el.div(
                rx.image(
                    src="/assortment_groundnut_products.png",
                    alt="Assortment of groundnuts and honey",
                    class_name="h-56 w-full object-cover sm:h-72 md:h-96 lg:w-full lg:h-full opacity-80 hover:opacity-100 transition-opacity duration-700",
                ),
                rx.el.div(
                    class_name="absolute inset-0 bg-gradient-to-l from-transparent to-[#050505]"
                ),
                class_name="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2 overflow-hidden",
            ),
            class_name="relative bg-[#050505] overflow-hidden border-b border-[#FFB800]/20",
        ),
        class_name="pt-20",
    )