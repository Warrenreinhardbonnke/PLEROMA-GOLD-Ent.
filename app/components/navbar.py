import reflex as rx
from app.states.cart_state import CartState
from app.states.ui_state import UIState
from app.states.auth_state import AuthState
from app.components.auth_modal import auth_modal


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-[#8B4513] hover:text-[#DAA520] font-medium transition-colors",
    )


def mobile_navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        on_click=UIState.close_mobile_menu,
        class_name="block px-3 py-2 text-base font-medium text-[#8B4513] hover:text-[#DAA520] hover:bg-[#F5DEB3] rounded-md",
    )


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-gray-300 hover:text-[#FFB800] hover:shadow-[0_0_10px_#FFB800] font-medium transition-all duration-300 uppercase tracking-wider text-sm",
    )


def mobile_navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        on_click=UIState.close_mobile_menu,
        class_name="block px-3 py-2 text-base font-medium text-gray-300 hover:text-[#FFB800] hover:bg-white/5 rounded-md border-l-2 border-transparent hover:border-[#FFB800]",
    )


def user_menu() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                rx.icon("user", class_name="h-5 w-5 mr-2"),
                AuthState.user_name,
                rx.icon("chevron-down", class_name="h-4 w-4 ml-1"),
                class_name="flex items-center text-[#FFB800] hover:text-white font-medium focus:outline-none transition-colors",
            ),
            class_name="peer group relative",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "My Profile",
                    href="/profile",
                    class_name="block px-4 py-2 text-sm text-gray-300 hover:bg-[#FFB800]/10 hover:text-[#FFB800]",
                ),
                rx.el.a(
                    "My Orders",
                    href="/orders",
                    class_name="block px-4 py-2 text-sm text-gray-300 hover:bg-[#FFB800]/10 hover:text-[#FFB800]",
                ),
                rx.el.a(
                    "Wishlist",
                    href="/wishlist",
                    class_name="block px-4 py-2 text-sm text-gray-300 hover:bg-[#FFB800]/10 hover:text-[#FFB800]",
                ),
                rx.el.button(
                    "Sign out",
                    on_click=AuthState.logout,
                    class_name="block w-full text-left px-4 py-2 text-sm text-red-400 hover:bg-red-500/10 hover:text-red-300 border-t border-white/10",
                ),
                class_name="py-1",
            ),
            class_name="hidden peer-hover:block hover:block absolute right-0 w-48 rounded-md shadow-[0_0_15px_rgba(0,0,0,0.5)] bg-[#0F0F12] border border-[#FFB800]/30 backdrop-blur-xl z-50",
        ),
        class_name="relative ml-4",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        auth_modal(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.a(
                            rx.el.div(
                                rx.icon(
                                    "hexagon", class_name="h-8 w-8 text-[#FFB800] mr-2"
                                ),
                                class_name="animate-pulse",
                            ),
                            rx.el.span(
                                "PLEROMA", class_name="text-white tracking-[0.2em]"
                            ),
                            rx.el.span(
                                "GOLD",
                                class_name="text-[#FFB800] tracking-[0.2em] font-bold drop-shadow-[0_0_5px_#FFB800]",
                            ),
                            class_name="flex items-center text-xl font-bold",
                            href="/",
                        ),
                        class_name="flex-shrink-0 flex items-center",
                    ),
                    rx.el.div(
                        rx.el.div(
                            navbar_link("Home", "/"),
                            navbar_link("Products", "/products"),
                            navbar_link("About", "/about"),
                            navbar_link("Contact", "/contact"),
                            class_name="ml-10 flex items-baseline space-x-8",
                        ),
                        class_name="hidden md:block",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.a(
                                rx.el.div(
                                    rx.icon(
                                        "shopping-cart",
                                        class_name="h-5 w-5 text-white hover:text-[#FFB800] transition-colors",
                                    ),
                                    rx.cond(
                                        CartState.total_items > 0,
                                        rx.el.span(
                                            CartState.total_items,
                                            class_name="absolute -top-2 -right-2 bg-[#FFB800] text-black text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center shadow-[0_0_10px_#FFB800]",
                                        ),
                                        rx.fragment(),
                                    ),
                                    class_name="relative p-2 border border-white/10 rounded-lg hover:border-[#FFB800]/50 hover:bg-[#FFB800]/10 transition-all",
                                ),
                                href="/cart",
                            ),
                            class_name="ml-4 flex items-center md:ml-6",
                        ),
                        rx.cond(
                            AuthState.is_logged_in,
                            user_menu(),
                            rx.el.button(
                                "LOGIN",
                                on_click=AuthState.toggle_login_modal,
                                class_name="ml-4 px-6 py-2 rounded-sm bg-transparent border border-[#FFB800] text-[#FFB800] text-sm font-bold hover:bg-[#FFB800] hover:text-black transition-all duration-300 hidden md:block tracking-wider shadow-[0_0_10px_rgba(255,184,0,0.2)] hover:shadow-[0_0_20px_rgba(255,184,0,0.6)] clip-path-polygon-[10%_0,100%_0,100%_70%,90%_100%,0_100%,0_30%]",
                            ),
                        ),
                        rx.el.div(
                            rx.el.button(
                                rx.cond(
                                    UIState.mobile_menu_open,
                                    rx.icon("x", class_name="h-6 w-6 text-[#FFB800]"),
                                    rx.icon(
                                        "menu", class_name="h-6 w-6 text-[#FFB800]"
                                    ),
                                ),
                                on_click=UIState.toggle_mobile_menu,
                                class_name="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-white/10 focus:outline-none",
                            ),
                            class_name="-mr-2 flex md:hidden ml-4",
                        ),
                        class_name="flex items-center",
                    ),
                    class_name="flex items-center justify-between h-20",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#050505]/80 backdrop-blur-md border-b border-[#FFB800]/20 fixed w-full z-50 top-0 shadow-[0_5px_30px_rgba(0,0,0,0.5)]",
        ),
        rx.cond(
            UIState.mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    mobile_navbar_link("Home", "/"),
                    mobile_navbar_link("Products", "/products"),
                    mobile_navbar_link("About", "/about"),
                    mobile_navbar_link("Contact", "/contact"),
                    rx.cond(
                        AuthState.is_logged_in,
                        rx.fragment(
                            mobile_navbar_link("My Profile", "/profile"),
                            mobile_navbar_link("My Orders", "/orders"),
                            mobile_navbar_link("Wishlist", "/wishlist"),
                            rx.el.button(
                                "Sign Out",
                                on_click=AuthState.logout,
                                class_name="block w-full text-left px-3 py-2 text-base font-medium text-red-600 hover:bg-red-50 rounded-md",
                            ),
                        ),
                        rx.el.button(
                            "Login / Sign Up",
                            on_click=[
                                AuthState.toggle_login_modal,
                                UIState.close_mobile_menu,
                            ],
                            class_name="block w-full text-left px-3 py-2 text-base font-medium text-[#8B4513] hover:text-[#DAA520] hover:bg-[#F5DEB3] rounded-md",
                        ),
                    ),
                    class_name="px-2 pt-2 pb-3 space-y-1 sm:px-3",
                ),
                class_name="md:hidden bg-white fixed w-full z-40 top-16 shadow-lg border-b border-[#DAA520]/20",
            ),
            rx.fragment(),
        ),
    )