import reflex as rx
from app.components.admin_sidebar import admin_layout
from app.states.admin_state import AdminState

TOOLTIP_PROPS = {
    "content_style": {
        "backgroundColor": "white",
        "borderRadius": "8px",
        "border": "1px solid #e5e7eb",
        "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
    },
    "item_style": {"color": "#374151", "fontSize": "14px", "fontWeight": "500"},
    "separator": "",
}


def reports_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Analytics & Reports", class_name="text-2xl font-bold text-gray-900 mb-6"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Total Revenue", class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.p(
                    AdminState.revenue_formatted,
                    class_name="text-2xl font-bold text-gray-900 mt-2",
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
            ),
            rx.el.div(
                rx.el.h3(
                    "Avg. Order Value", class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.p(
                    "KES 8,500", class_name="text-2xl font-bold text-gray-900 mt-2"
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
            ),
            rx.el.div(
                rx.el.h3(
                    "Conversion Rate", class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.p("3.2%", class_name="text-2xl font-bold text-gray-900 mt-2"),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Sales Performance",
                    class_name="text-lg font-bold text-gray-900 mb-4",
                ),
                rx.recharts.bar_chart(
                    rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False),
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.x_axis(
                        data_key="name", tick_line=False, axis_line=False
                    ),
                    rx.recharts.y_axis(tick_line=False, axis_line=False),
                    rx.recharts.bar(
                        data_key="sales", fill="#8B4513", radius=[4, 4, 0, 0]
                    ),
                    data=AdminState.sales_data,
                    height=300,
                    width="100%",
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
            ),
            rx.el.div(
                rx.el.h3(
                    "Sales by Category",
                    class_name="text-lg font-bold text-gray-900 mb-4",
                ),
                rx.recharts.pie_chart(
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.pie(
                        data=AdminState.category_data,
                        data_key="value",
                        name_key="name",
                        cx="50%",
                        cy="50%",
                        inner_radius=60,
                        outer_radius=80,
                        fill="#8884d8",
                        label=True,
                        stroke="#fff",
                        stroke_width=2,
                    ),
                    height=300,
                    width="100%",
                ),
                class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        class_name="p-6 max-w-7xl mx-auto",
    )


def admin_reports_page() -> rx.Component:
    return admin_layout(reports_content())