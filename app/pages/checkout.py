import reflex as rx
from app.states.cart_state import CartState
from app.states.checkout_state import CheckoutState
from app.components.navbar import navbar
from app.components.footer import footer


def checkout_input(
    label: str, placeholder: str, field_name: str, error_var: str, type_: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=field_name,
            class_name="block text-sm font-medium text-gray-700",
        ),
        rx.el.div(
            rx.el.input(
                type=type_,
                name=field_name,
                id=field_name,
                placeholder=placeholder,
                on_change=lambda v: CheckoutState.set_field(field_name, v),
                class_name="block w-full shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm border-gray-300 rounded-md px-4 py-3 border mt-1",
            ),
            rx.cond(
                error_var != "",
                rx.el.p(error_var, class_name="mt-1 text-sm text-red-600"),
            ),
            class_name="mt-1",
        ),
        class_name="col-span-6 sm:col-span-4",
    )


def delivery_option(
    title: str, price: str, description: str, value: str
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            rx.el.input(
                type="radio",
                name="delivery-method",
                value=value,
                checked=CheckoutState.delivery_method == value,
                on_change=lambda: CheckoutState.set_delivery_method(value),
                class_name="h-4 w-4 text-[#8B4513] focus:ring-[#DAA520] border-gray-300",
            ),
            rx.el.div(
                rx.el.span(title, class_name="block text-sm font-medium text-gray-900"),
                rx.el.span(description, class_name="block text-sm text-gray-500"),
                rx.el.span(
                    price, class_name="block text-sm font-medium text-gray-900 mt-1"
                ),
                class_name="ml-3 flex flex-col",
            ),
            class_name="flex items-center cursor-pointer p-4 border rounded-lg hover:bg-gray-50 transition-colors",
        ),
        class_name="mb-4",
    )


def payment_option(id: str, name: str, icon_name: str) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            rx.el.input(
                type="radio",
                name="payment-method",
                value=id,
                checked=CheckoutState.payment_method == id,
                on_change=lambda: CheckoutState.set_payment_method(id),
                class_name="h-4 w-4 text-[#8B4513] focus:ring-[#DAA520] border-gray-300",
            ),
            rx.el.span(name, class_name="ml-3 block text-sm font-medium text-gray-700"),
            rx.icon(icon_name, class_name="ml-auto h-5 w-5 text-gray-400"),
            class_name="flex items-center cursor-pointer p-4 border rounded-lg hover:bg-gray-50 transition-colors",
        ),
        class_name="mb-3",
    )


def checkout_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Checkout",
                        class_name="text-3xl font-extrabold tracking-tight text-[#8B4513] sm:text-4xl mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.el.h2(
                                    "Contact Information",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    checkout_input(
                                        "Full Name",
                                        "John Doe",
                                        "name",
                                        CheckoutState.name_error,
                                    ),
                                    checkout_input(
                                        "Email Address",
                                        "john@example.com",
                                        "email",
                                        CheckoutState.email_error,
                                        "email",
                                    ),
                                    checkout_input(
                                        "Phone Number",
                                        "+254 700 000 000",
                                        "phone",
                                        CheckoutState.phone_error,
                                        "tel",
                                    ),
                                    class_name="grid grid-cols-1 gap-y-6 sm:grid-cols-2 sm:gap-x-4 mb-8",
                                ),
                                rx.el.h2(
                                    "Shipping Address",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    checkout_input(
                                        "Address",
                                        "123 Street Name",
                                        "address",
                                        CheckoutState.address_error,
                                    ),
                                    checkout_input(
                                        "City / Town", "Nairobi", "city", ""
                                    ),
                                    class_name="grid grid-cols-1 gap-y-6 sm:grid-cols-2 sm:gap-x-4 mb-8",
                                ),
                                rx.el.h2(
                                    "Delivery Method",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    delivery_option(
                                        "Standard Delivery",
                                        "Free",
                                        "3-5 business days",
                                        "Standard",
                                    ),
                                    delivery_option(
                                        "Express Delivery",
                                        "KES 200",
                                        "1-2 business days",
                                        "Express",
                                    ),
                                    class_name="mb-8",
                                ),
                                rx.el.h2(
                                    "Payment Method",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    payment_option(
                                        "M-Pesa", "M-Pesa (STK Push)", "smartphone"
                                    ),
                                    payment_option(
                                        "Manual M-Pesa",
                                        "Manual M-Pesa (Send Money)",
                                        "smartphone",
                                    ),
                                    payment_option(
                                        "Card", "Credit / Debit Card", "credit-card"
                                    ),
                                    payment_option(
                                        "COD", "Cash on Delivery", "banknote"
                                    ),
                                    class_name="mb-8",
                                ),
                                rx.cond(
                                    CheckoutState.payment_method == "M-Pesa",
                                    rx.el.div(
                                        rx.el.label(
                                            "M-Pesa Phone Number",
                                            class_name="block text-sm font-medium text-gray-700 mb-1",
                                        ),
                                        rx.el.input(
                                            type="tel",
                                            placeholder="e.g. 0712345678",
                                            default_value=CheckoutState.mpesa_phone,
                                            on_change=lambda v: CheckoutState.set_field(
                                                "mpesa_phone", v
                                            ),
                                            class_name="block w-full shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm border-gray-300 rounded-md px-4 py-3 border",
                                        ),
                                        rx.el.p(
                                            "You will receive a prompt on this number to enter your M-Pesa PIN.",
                                            class_name="mt-2 text-sm text-gray-500",
                                        ),
                                        class_name="mb-8 bg-[#F5DEB3]/20 p-4 rounded-lg border border-[#F5DEB3]",
                                    ),
                                ),
                                rx.cond(
                                    CheckoutState.payment_method == "Manual M-Pesa",
                                    rx.el.div(
                                        rx.el.h3(
                                            "Payment Instructions",
                                            class_name="text-sm font-bold text-[#8B4513] mb-2 uppercase tracking-wider",
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "Please send money to the following M-Pesa number:",
                                                class_name="text-sm text-gray-600 mb-2",
                                            ),
                                            rx.el.div(
                                                rx.el.span(
                                                    "M-Pesa Number:",
                                                    class_name="font-semibold text-gray-700",
                                                ),
                                                rx.el.span(
                                                    "0794807479",
                                                    class_name="ml-2 font-mono text-[#8B4513] font-bold",
                                                ),
                                                class_name="flex justify-between border-b border-[#8B4513]/10 py-1",
                                            ),
                                            rx.el.div(
                                                rx.el.span(
                                                    "Account Name:",
                                                    class_name="font-semibold text-gray-700",
                                                ),
                                                rx.el.span(
                                                    "Catherine Moraa",
                                                    class_name="ml-2 font-mono text-[#8B4513]",
                                                ),
                                                class_name="flex justify-between border-b border-[#8B4513]/10 py-1",
                                            ),
                                            rx.el.div(
                                                rx.el.span(
                                                    "Reference:",
                                                    class_name="font-semibold text-gray-700",
                                                ),
                                                rx.el.span(
                                                    "Your Order ID (Generated next)",
                                                    class_name="ml-2 font-mono text-[#8B4513]",
                                                ),
                                                class_name="flex justify-between py-1",
                                            ),
                                            class_name="bg-white/50 rounded p-3 mb-3",
                                        ),
                                        rx.el.p(
                                            "Your order will be confirmed once payment is verified. Please proceed to place your order.",
                                            class_name="text-xs text-gray-500 italic",
                                        ),
                                        class_name="mb-8 bg-[#FFB800]/10 p-5 rounded-lg border border-[#FFB800]/30",
                                    ),
                                ),
                            ),
                            class_name="lg:col-span-7",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h2(
                                    "Order Summary",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    rx.el.ul(
                                        rx.foreach(
                                            CartState.items,
                                            lambda item: rx.el.li(
                                                rx.el.div(
                                                    rx.image(
                                                        src=item["image"],
                                                        alt=item["name"],
                                                        class_name="h-16 w-16 rounded-md object-cover",
                                                    ),
                                                    rx.el.div(
                                                        rx.el.h4(
                                                            item["name"],
                                                            class_name="text-sm font-medium text-gray-700",
                                                        ),
                                                        rx.el.p(
                                                            f"Qty {item['quantity']}",
                                                            class_name="text-sm text-gray-500",
                                                        ),
                                                        class_name="ml-4",
                                                    ),
                                                    rx.el.p(
                                                        f"KES {item['price'].to(int) * item['quantity'].to(int)}",
                                                        class_name="ml-auto text-sm font-medium text-gray-900",
                                                    ),
                                                    class_name="flex items-center",
                                                ),
                                                class_name="py-4",
                                            ),
                                        ),
                                        class_name="divide-y divide-gray-200 border-b border-gray-200",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.dt(
                                                "Subtotal",
                                                class_name="text-sm text-gray-600",
                                            ),
                                            rx.el.dd(
                                                f"KES {CartState.subtotal}",
                                                class_name="text-sm font-medium text-gray-900",
                                            ),
                                            class_name="flex items-center justify-between py-2",
                                        ),
                                        rx.el.div(
                                            rx.el.dt(
                                                "Shipping",
                                                class_name="text-sm text-gray-600",
                                            ),
                                            rx.el.dd(
                                                f"KES {CheckoutState.delivery_fee}",
                                                class_name="text-sm font-medium text-gray-900",
                                            ),
                                            class_name="flex items-center justify-between py-2",
                                        ),
                                        rx.el.div(
                                            rx.el.dt(
                                                "Discount",
                                                class_name="text-sm text-gray-600",
                                            ),
                                            rx.el.dd(
                                                f"- KES {CartState.discount_amount}",
                                                class_name="text-sm font-medium text-green-600",
                                            ),
                                            class_name="flex items-center justify-between py-2",
                                        ),
                                        rx.el.div(
                                            rx.el.dt(
                                                "Total",
                                                class_name="text-base font-bold text-gray-900",
                                            ),
                                            rx.el.dd(
                                                f"KES {CheckoutState.final_total}",
                                                class_name="text-base font-bold text-[#8B4513]",
                                            ),
                                            class_name="flex items-center justify-between border-t border-gray-200 pt-4 mt-4",
                                        ),
                                        class_name="mt-4",
                                    ),
                                    rx.el.button(
                                        rx.cond(
                                            CheckoutState.is_processing_payment,
                                            rx.el.div(
                                                rx.spinner(color="white", size="2"),
                                                rx.el.span(
                                                    "Processing...", class_name="ml-2"
                                                ),
                                                class_name="flex items-center justify-center",
                                            ),
                                            "Place Order",
                                        ),
                                        on_click=CheckoutState.place_order,
                                        disabled=CheckoutState.is_processing_payment,
                                        class_name="w-full mt-6 bg-[#8B4513] border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513] disabled:opacity-50 disabled:cursor-not-allowed",
                                    ),
                                    class_name="bg-gray-50 rounded-lg px-4 py-6 sm:p-6 lg:p-8",
                                ),
                            ),
                            class_name="lg:col-span-5 mt-10 lg:mt-0",
                        ),
                        class_name="lg:grid lg:grid-cols-12 lg:gap-x-12 lg:items-start",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 bg-white",
            ),
            class_name="flex-grow bg-white",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )