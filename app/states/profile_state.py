import reflex as rx


class ProfileState(rx.State):
    full_name: str = "John Doe"
    email: str = "john@example.com"
    phone: str = "+254 700 000 000"
    dob: str = "1990-01-01"
    gender: str = "Male"
    address: str = "123 Street Name"
    city: str = "Nairobi"
    postal_code: str = "00100"

    @rx.event
    def set_field(self, field: str, value: str):
        setattr(self, field, value)

    @rx.event
    def save_changes(self):
        return rx.toast(
            "Profile updated successfully!",
            position="bottom-right",
            duration=3000,
            close_button=True,
        )