import reflex as rx
from app.states.auth_state import AuthState


def sidebar_item(icon: str, text: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5 mr-3"),
        rx.el.span(text),
        href=url,
        class_name="flex items-center px-4 py-3 text-gray-400 hover:bg-[#FFB800]/10 hover:text-[#FFB800] hover:border-l-2 hover:border-[#FFB800] transition-all mb-1",
    )


def admin_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.el.span("PLEROMA GOLD", class_name="text-[#FFB800]"),
                rx.el.span(" ADMIN", class_name="text-white text-sm tracking-[0.3em]"),
                class_name="text-xl font-bold tracking-tight font-['Rajdhani']",
                href="/admin",
            ),
            class_name="h-20 flex items-center px-6 border-b border-white/10",
        ),
        rx.el.nav(
            sidebar_item("layout-dashboard", "Dashboard", "/admin"),
            sidebar_item("package", "Products", "/admin/products"),
            sidebar_item("shopping-bag", "Orders", "/admin/orders"),
            sidebar_item("users", "Customers", "/admin/customers"),
            sidebar_item("bar-chart", "Reports", "/admin/reports"),
            sidebar_item("book-open", "M-Pesa Guide", "/admin/mpesa-guide"),
            class_name="p-4 space-y-1",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("log-out", class_name="h-5 w-5 mr-3"),
                rx.el.span("Sign Out"),
                on_click=AuthState.logout,
                class_name="flex items-center w-full px-4 py-3 text-gray-400 hover:bg-red-900/20 hover:text-red-400 transition-colors",
            ),
            class_name="absolute bottom-0 w-full p-4 border-t border-white/10",
        ),
        class_name="hidden lg:flex flex-col w-64 bg-[#050505] border-r border-white/10 h-screen fixed left-0 top-0 z-30",
    )


def admin_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.h2(
                "OVERSEER NODE",
                class_name="text-lg font-bold text-[#FFB800] font-['Rajdhani'] tracking-widest",
            ),
            rx.el.div(
                rx.el.span(
                    "Admin Online",
                    class_name="text-sm font-medium text-green-400 mr-4 uppercase tracking-wider",
                ),
                rx.image(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed=Admin",
                    class_name="h-8 w-8 rounded-full bg-gray-800 border border-[#FFB800]/50",
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between h-20 px-8 bg-[#050505] border-b border-white/10",
        ),
        class_name="lg:pl-64",
    )


def admin_layout(content: rx.Component) -> rx.Component:
    return rx.cond(
        AuthState.is_admin,
        rx.el.div(
            admin_sidebar(),
            admin_header(),
            rx.el.main(content, class_name="lg:pl-64 pt-4 min-h-screen bg-[#0A0A0C]"),
            class_name="min-h-screen bg-[#0A0A0C] font-['Inter']",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "lock",
                    class_name="h-16 w-16 text-[#FFB800] mb-4 mx-auto animate-pulse",
                ),
                rx.el.h1(
                    "ACCESS DENIED",
                    class_name="text-3xl font-bold text-white mb-2 font-['Rajdhani'] tracking-widest",
                ),
                rx.el.p(
                    "Security protocol initiated. Administrator credentials required.",
                    class_name="text-gray-500 mb-8",
                ),
                rx.el.a(
                    "RETURN TO BASE",
                    href="/",
                    class_name="inline-flex items-center px-8 py-3 border border-[#FFB800] text-sm font-bold text-[#FFB800] hover:bg-[#FFB800] hover:text-black transition-all",
                ),
                class_name="text-center p-12 border border-[#FFB800]/20 bg-[#050505] shadow-[0_0_50px_rgba(255,184,0,0.1)]",
            ),
            class_name="min-h-screen flex items-center justify-center bg-[#000000]",
        ),
    )