import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def contact_info_card(icon: str, title: str, content: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-[#8B4513]"),
            class_name="flex items-center justify-center h-12 w-12 rounded-full bg-[#F5DEB3] mb-4",
        ),
        rx.el.h3(title, class_name="text-lg font-medium text-gray-900 mb-2"),
        rx.el.div(
            rx.foreach(content, lambda c: rx.el.p(c, class_name="text-gray-500")),
            class_name="text-center",
        ),
        class_name="flex flex-col items-center p-6 bg-white rounded-lg shadow-sm border border-gray-100",
    )


def contact_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Get in Touch",
                        class_name="text-4xl font-extrabold text-[#8B4513] text-center mb-4",
                    ),
                    rx.el.p(
                        "We'd love to hear from you. Send us a message or visit our store.",
                        class_name="text-xl text-gray-500 text-center max-w-2xl mx-auto",
                    ),
                    class_name="py-16 bg-[#F5DEB3]/20",
                ),
                rx.el.div(
                    rx.el.div(
                        contact_info_card(
                            "phone", "Phone", ["+254 700 000 000", "+254 722 123 456"]
                        ),
                        contact_info_card(
                            "mail",
                            "Email",
                            ["info@pleromagold.co.ke", "sales@pleromagold.co.ke"],
                        ),
                        contact_info_card(
                            "map-pin",
                            "Location",
                            ["123 Pleroma Gold Plaza, Nairobi", "Kenya"],
                        ),
                        contact_info_card(
                            "clock",
                            "Business Hours",
                            ["Mon - Fri: 8am - 6pm", "Sat: 9am - 4pm"],
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16 -mt-10 relative z-10",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h2(
                                "Send us a Message",
                                class_name="text-2xl font-bold text-[#8B4513] mb-6",
                            ),
                            rx.el.form(
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.label(
                                            "Name",
                                            class_name="block text-sm font-medium text-gray-700 mb-1",
                                        ),
                                        rx.el.input(
                                            type="text",
                                            class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-[#DAA520] focus:ring-[#DAA520] py-3 px-4 border",
                                        ),
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            "Email",
                                            class_name="block text-sm font-medium text-gray-700 mb-1",
                                        ),
                                        rx.el.input(
                                            type="email",
                                            class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-[#DAA520] focus:ring-[#DAA520] py-3 px-4 border",
                                        ),
                                    ),
                                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Subject",
                                        class_name="block text-sm font-medium text-gray-700 mb-1",
                                    ),
                                    rx.el.input(
                                        type="text",
                                        class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-[#DAA520] focus:ring-[#DAA520] py-3 px-4 border mb-6",
                                    ),
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        "Message",
                                        class_name="block text-sm font-medium text-gray-700 mb-1",
                                    ),
                                    rx.el.textarea(
                                        rows=5,
                                        class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-[#DAA520] focus:ring-[#DAA520] py-3 px-4 border mb-6",
                                    ),
                                ),
                                rx.el.button(
                                    "Send Message",
                                    class_name="w-full bg-[#8B4513] text-white font-medium py-3 px-4 rounded-md hover:bg-[#6d360f] transition-colors shadow-md hover:shadow-lg",
                                ),
                            ),
                            class_name="bg-white p-8 rounded-lg shadow-lg border border-gray-100",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h2(
                                    "Chat on WhatsApp",
                                    class_name="text-2xl font-bold text-white mb-4",
                                ),
                                rx.el.p(
                                    "Need quick assistance? Chat with us directly on WhatsApp for instant support.",
                                    class_name="text-white/90 mb-8",
                                ),
                                rx.el.a(
                                    rx.icon(
                                        "message-circle", class_name="w-6 h-6 mr-2"
                                    ),
                                    "Start Chat",
                                    href="https://wa.me/254700000000",
                                    class_name="inline-flex items-center px-6 py-3 bg-white text-green-600 font-bold rounded-full shadow-lg hover:bg-gray-50 transition-colors",
                                ),
                                class_name="bg-green-500 p-8 rounded-lg shadow-lg text-center mb-8",
                            ),
                            rx.image(
                                src="/placeholder.svg",
                                class_name="w-full h-64 object-cover rounded-lg shadow-lg",
                            ),
                            class_name="space-y-8",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-12",
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16",
                ),
            ),
            class_name="flex-grow",
        ),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )