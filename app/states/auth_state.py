import reflex as rx


class AuthState(rx.State):
    show_login: bool = False
    is_logged_in: bool = False
    is_admin: bool = True
    active_tab: str = "login"
    user_name: str = "John Doe"

    @rx.event
    def toggle_login_modal(self):
        self.show_login = not self.show_login

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def login(self):
        self.is_logged_in = True
        self.show_login = False
        return rx.toast(
            "Logged in successfully!",
            position="bottom-right",
            duration=3000,
            close_button=True,
        )

    @rx.event
    def signup(self):
        self.is_logged_in = True
        self.show_login = False
        return rx.toast(
            "Account created successfully!",
            position="bottom-right",
            duration=3000,
            close_button=True,
        )

    @rx.event
    def logout(self):
        self.is_logged_in = False
        return rx.redirect("/")