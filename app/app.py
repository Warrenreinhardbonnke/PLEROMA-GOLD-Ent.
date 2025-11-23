import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.features import features
from app.components.featured_products import featured_products
from app.components.footer import footer
from app.pages.products import products_page
from app.pages.product_detail import product_detail_page
from app.pages.cart import cart_page
from app.pages.checkout import checkout_page
from app.pages.order_confirmation import order_confirmation_page
from app.pages.profile import profile_page
from app.pages.orders import orders_page
from app.pages.order_tracking import order_tracking_page
from app.pages.wishlist import wishlist_page
from app.pages.contact import contact_page
from app.pages.about import about_page
from app.states.product_state import ProductState
from app.states.order_state import OrderState


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(hero(), features(), featured_products()),
        footer(),
        class_name="font-['Rajdhani'] bg-[#050505] min-h-screen flex flex-col text-gray-100 selection:bg-[#FFB800] selection:text-black",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Inter:wght@400;600&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(products_page, route="/products", on_load=ProductState.on_load)
app.add_page(
    product_detail_page,
    route="/product/[id]",
    on_load=[ProductState.reset_detail_state, ProductState.on_load],
)
app.add_page(cart_page, route="/cart", on_load=ProductState.on_load)
app.add_page(checkout_page, route="/checkout", on_load=ProductState.on_load)
app.add_page(
    order_confirmation_page, route="/order-confirmation", on_load=ProductState.on_load
)
app.add_page(profile_page, route="/profile")
app.add_page(orders_page, route="/orders", on_load=OrderState.on_load)
app.add_page(order_tracking_page, route="/track-order/[order_id]")
app.add_page(wishlist_page, route="/wishlist")
app.add_page(contact_page, route="/contact")
app.add_page(about_page, route="/about")
from app.pages.admin.dashboard import admin_dashboard_page
from app.pages.admin.products import admin_products_page
from app.pages.admin.orders import admin_orders_page
from app.pages.admin.customers import admin_customers_page
from app.pages.admin.reports import admin_reports_page
from app.states.admin_state import AdminState
from app.states.admin_product_state import AdminProductState
from app.states.admin_order_state import AdminOrderState

app.add_page(admin_dashboard_page, route="/admin", on_load=AdminState.on_load)
app.add_page(
    admin_products_page, route="/admin/products", on_load=AdminProductState.on_load
)
app.add_page(admin_orders_page, route="/admin/orders", on_load=AdminOrderState.on_load)
app.add_page(admin_customers_page, route="/admin/customers")
app.add_page(admin_reports_page, route="/admin/reports")