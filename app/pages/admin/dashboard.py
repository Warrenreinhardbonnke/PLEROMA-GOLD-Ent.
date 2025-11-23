import reflex as rx
from app.components.admin_sidebar import admin_layout
from app.states.admin_state import AdminState

TOOLTIP_PROPS = {
    "content_style": {
        "backgroundColor": "#0A0A0C",
        "borderRadius": "4px",
        "border": "1px solid #333",
        "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.5)",
        "color": "#fff",
    },
    "item_style": {"color": "#FFB800", "fontSize": "14px", "fontWeight": "500"},
    "separator": "",
}


def stat_card(
    title: str, value: str, icon: str, color: str, trend: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    title,
                    class_name="text-sm font-medium text-gray-400 uppercase tracking-wider",
                ),
                rx.el.p(
                    value, class_name="mt-1 text-2xl font-bold text-white font-mono"
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.icon(icon, class_name=f"h-6 w-6 text-[#FFB800]"),
                class_name=f"flex items-center justify-center h-12 w-12 rounded-none bg-[#FFB800]/10 border border-[#FFB800]/30",
            ),
            class_name="flex items-center",
        ),
        rx.el.div(
            rx.el.span(
                f"+{trend}%",
                class_name="text-[#FFB800] text-sm font-medium flex items-center",
            ),
            rx.el.span("since last cycle", class_name="ml-2 text-sm text-gray-500"),
            class_name="mt-4 flex items-center",
        ),
        class_name="bg-[#0A0A0C] p-6 border border-white/5 hover:border-[#FFB800]/30 transition-all hover:shadow-[0_0_20px_rgba(255,184,0,0.1)]",
    )


def activity_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name="h-2 w-2 bg-[#FFB800] mt-2 shadow-[0_0_5px_#FFB800]"),
            class_name="flex flex-col items-center mr-4",
        ),
        rx.el.div(
            rx.el.p(item["action"], class_name="text-sm font-medium text-gray-300"),
            rx.el.p(item["time"], class_name="text-xs text-gray-600"),
            class_name="pb-4 border-l border-white/10 pl-4 ml-[-5px]",
        ),
        class_name="flex",
    )


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "COMMAND CENTER",
            class_name="text-2xl font-bold text-white mb-6 tracking-widest font-['Rajdhani']",
        ),
        rx.el.div(
            stat_card(
                "Total Revenue",
                AdminState.revenue_formatted,
                "dollar-sign",
                "green",
                "12",
            ),
            stat_card(
                "Total Orders",
                AdminState.total_orders.to_string(),
                "shopping-bag",
                "blue",
                "8",
            ),
            stat_card(
                "Customers",
                AdminState.total_customers.to_string(),
                "users",
                "purple",
                "15",
            ),
            stat_card(
                "Growth", f"{AdminState.growth_rate}%", "trending-up", "yellow", "4"
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "REVENUE STREAM",
                    class_name="text-lg font-bold text-white mb-4 font-['Rajdhani'] tracking-wider",
                ),
                rx.recharts.area_chart(
                    rx.recharts.cartesian_grid(
                        stroke_dasharray="3 3", vertical=False, stroke="#333"
                    ),
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.x_axis(
                        data_key="name", tick_line=False, axis_line=False, stroke="#666"
                    ),
                    rx.recharts.y_axis(tick_line=False, axis_line=False, stroke="#666"),
                    rx.recharts.area(
                        data_key="revenue",
                        type_="monotone",
                        stroke="#FFB800",
                        fill="#FFB800",
                        fill_opacity=0.2,
                        stroke_width=2,
                    ),
                    data=AdminState.sales_data,
                    height=300,
                    width="100%",
                ),
                class_name="bg-[#0A0A0C] p-6 border border-white/5",
            ),
            rx.el.div(
                rx.el.h2(
                    "SYSTEM LOGS",
                    class_name="text-lg font-bold text-white mb-4 font-['Rajdhani'] tracking-wider",
                ),
                rx.el.div(
                    rx.foreach(AdminState.recent_activity, activity_item),
                    class_name="mt-4",
                ),
                class_name="bg-[#0A0A0C] p-6 border border-white/5",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8",
        ),
        class_name="p-6 max-w-7xl mx-auto",
    )


def admin_dashboard_page() -> rx.Component:
    return admin_layout(dashboard_content())