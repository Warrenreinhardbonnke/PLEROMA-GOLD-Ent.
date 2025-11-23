import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def value_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8 text-[#DAA520]"),
            class_name="flex items-center justify-center h-16 w-16 rounded-full bg-[#F5DEB3]/30 mb-6 mx-auto",
        ),
        rx.el.h3(title, class_name="text-xl font-bold text-[#8B4513] mb-4 text-center"),
        rx.el.p(description, class_name="text-gray-600 text-center leading-relaxed"),
        class_name="p-8 bg-white rounded-xl shadow-sm hover:shadow-md transition-shadow border border-gray-100",
    )


def about_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Our Story",
                        class_name="text-4xl font-extrabold text-[#8B4513] sm:text-5xl mb-6",
                    ),
                    rx.el.p(
                        "Bringing nature's finest treasures from local farms to your table.",
                        class_name="text-xl text-gray-600 max-w-3xl mx-auto",
                    ),
                    class_name="text-center py-20 bg-[#F5DEB3]/20",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h2(
                                "Rooted in Quality",
                                class_name="text-3xl font-bold text-[#8B4513] mb-6",
                            ),
                            rx.el.p(
                                "PLEROMA GOLD FOODS began with a simple mission: to provide wholesome, natural foods that nourish the body and delight the senses. We started as a small family business, sourcing premium groundnuts from trusted local farmers who share our commitment to sustainable agriculture.",
                                class_name="text-lg text-gray-600 mb-6 leading-relaxed",
                            ),
                            rx.el.p(
                                "Today, we continue to roast our nuts in small batches to ensure maximum freshness and flavor. Our honey is harvested from pristine forests, untouched by additives or processing. We believe that food should be simple, honest, and delicious.",
                                class_name="text-lg text-gray-600 leading-relaxed",
                            ),
                            class_name="lg:pr-12",
                        ),
                        rx.el.div(
                            rx.image(
                                src="/placeholder.svg",
                                class_name="rounded-xl shadow-xl w-full h-full object-cover",
                            ),
                            class_name="h-96 lg:h-auto",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-24",
                    ),
                    rx.el.div(
                        rx.el.h2(
                            "Our Core Values",
                            class_name="text-3xl font-bold text-[#8B4513] text-center mb-16",
                        ),
                        rx.el.div(
                            value_card(
                                "leaf",
                                "100% Natural",
                                "We never use artificial preservatives, colors, or flavors. Everything we make comes straight from nature.",
                            ),
                            value_card(
                                "heart",
                                "Passion for Quality",
                                "We obsess over every detail, from selecting the best raw materials to packaging the final product with care.",
                            ),
                            value_card(
                                "users",
                                "Community First",
                                "We support local farmers and believe in building strong, lasting relationships with our community.",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-3 gap-8 mb-24",
                        ),
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h2(
                                "Join the PLEROMA GOLD Family",
                                class_name="text-3xl font-bold text-white mb-6",
                            ),
                            rx.el.p(
                                "Experience the authentic taste of our premium products. Healthy, delicious, and always fresh.",
                                class_name="text-xl text-white/90 mb-8 max-w-2xl mx-auto",
                            ),
                            rx.el.a(
                                "Shop Now",
                                href="/products",
                                class_name="inline-flex items-center px-8 py-4 border-2 border-white text-lg font-bold rounded-md text-white hover:bg-white hover:text-[#8B4513] transition-colors",
                            ),
                            class_name="text-center",
                        ),
                        class_name="bg-[#8B4513] rounded-2xl p-12 shadow-xl",
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
                ),
            ),
            class_name="flex-grow",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )