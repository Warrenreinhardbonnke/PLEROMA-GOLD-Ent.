import reflex as rx
from app.states.auth_state import AuthState


def auth_input(
    placeholder: str, type_: str = "text", icon: str = "user"
) -> rx.Component:
    return rx.el.div(
        rx.icon(
            icon,
            class_name="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400",
        ),
        rx.el.input(
            type=type_,
            placeholder=placeholder,
            class_name="pl-10 block w-full border-gray-300 rounded-md shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm py-3 border",
        ),
        class_name="relative rounded-md shadow-sm mb-4",
    )


def login_form() -> rx.Component:
    return rx.el.div(
        auth_input("Email address", "email", "mail"),
        auth_input("Password", "password", "lock"),
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    type="checkbox",
                    class_name="h-4 w-4 text-[#8B4513] focus:ring-[#DAA520] border-gray-300 rounded",
                ),
                rx.el.label(
                    "Remember me", class_name="ml-2 block text-sm text-gray-900"
                ),
                class_name="flex items-center",
            ),
            rx.el.a(
                "Forgot password?",
                href="#",
                class_name="text-sm font-medium text-[#8B4513] hover:text-[#DAA520]",
            ),
            class_name="flex items-center justify-between mb-6",
        ),
        rx.el.button(
            "Sign In",
            on_click=AuthState.login,
            class_name="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8B4513] hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513]",
        ),
    )


def signup_form() -> rx.Component:
    return rx.el.div(
        auth_input("Full Name", "text", "user"),
        auth_input("Email address", "email", "mail"),
        auth_input("Phone Number", "tel", "phone"),
        auth_input("Password", "password", "lock"),
        auth_input("Confirm Password", "password", "lock"),
        rx.el.button(
            "Create Account",
            on_click=AuthState.signup,
            class_name="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8B4513] hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513]",
        ),
    )


def auth_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-50"
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.radix.primitives.dialog.title(
                        "Welcome to PLEROMA GOLD",
                        class_name="text-2xl font-bold text-center text-[#8B4513] mb-2",
                    ),
                    rx.radix.primitives.dialog.description(
                        "Sign in to access your account and orders.",
                        class_name="text-center text-gray-500 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.button(
                                "Login",
                                on_click=lambda: AuthState.set_active_tab("login"),
                                class_name=rx.cond(
                                    AuthState.active_tab == "login",
                                    "flex-1 py-2 text-sm font-medium text-[#8B4513] border-b-2 border-[#8B4513]",
                                    "flex-1 py-2 text-sm font-medium text-gray-500 border-b border-gray-200 hover:text-gray-700",
                                ),
                            ),
                            rx.el.button(
                                "Sign Up",
                                on_click=lambda: AuthState.set_active_tab("signup"),
                                class_name=rx.cond(
                                    AuthState.active_tab == "signup",
                                    "flex-1 py-2 text-sm font-medium text-[#8B4513] border-b-2 border-[#8B4513]",
                                    "flex-1 py-2 text-sm font-medium text-gray-500 border-b border-gray-200 hover:text-gray-700",
                                ),
                            ),
                            class_name="flex mb-8",
                        ),
                        rx.cond(
                            AuthState.active_tab == "login", login_form(), signup_form()
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    class_name="w-full border-t border-gray-300"
                                ),
                                class_name="absolute inset-0 flex items-center",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    "Or continue with",
                                    class_name="px-2 bg-white text-gray-500",
                                ),
                                class_name="relative flex justify-center text-sm",
                            ),
                            class_name="relative mt-6 mb-6",
                        ),
                        rx.el.button(
                            rx.icon("mail", class_name="h-5 w-5 mr-2"),
                            "Continue with Google",
                            class_name="w-full flex justify-center items-center py-3 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                        ),
                    ),
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            rx.icon(
                                "x",
                                class_name="h-6 w-6 text-gray-400 hover:text-gray-500",
                            ),
                            class_name="absolute top-4 right-4",
                        )
                    ),
                    class_name="bg-white rounded-xl px-4 pt-5 pb-4 sm:p-6 sm:pb-4 max-w-md w-full",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-xl shadow-2xl w-full max-w-md z-50 focus:outline-none",
            ),
        ),
        open=AuthState.show_login,
        on_open_change=AuthState.toggle_login_modal,
    )