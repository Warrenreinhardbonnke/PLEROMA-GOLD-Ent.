import reflex as rx
from app.states.profile_state import ProfileState
from app.components.navbar import navbar
from app.components.footer import footer


def profile_field(
    label: str, value: str, field_name: str, type_: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            html_for=field_name,
            class_name="block text-sm font-medium text-gray-700",
        ),
        rx.el.input(
            type=type_,
            default_value=value,
            id=field_name,
            on_blur=lambda v: ProfileState.set_field(field_name, v),
            class_name="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-[#DAA520] focus:border-[#DAA520] sm:text-sm border px-4 py-2",
        ),
        class_name="col-span-6 sm:col-span-3",
    )


def profile_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "My Profile",
                            class_name="text-3xl font-extrabold text-[#8B4513]",
                        ),
                        rx.el.div(
                            rx.el.a(
                                "Home", href="/", class_name="hover:text-[#DAA520]"
                            ),
                            rx.el.span("/", class_name="mx-2 text-gray-400"),
                            rx.el.span("Profile", class_name="text-gray-500"),
                            class_name="flex items-center text-sm text-gray-500 mt-2",
                        ),
                        class_name="mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.image(
                                        src=f"https://api.dicebear.com/9.x/notionists/svg?seed={ProfileState.email}",
                                        class_name="h-32 w-32 rounded-full bg-gray-100 object-cover",
                                    ),
                                    rx.el.button(
                                        "Change Avatar",
                                        class_name="mt-4 px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50",
                                    ),
                                    class_name="flex flex-col items-center",
                                ),
                                class_name="p-6",
                            ),
                            class_name="md:col-span-1",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    "Personal Information",
                                    class_name="text-lg font-medium text-[#8B4513] mb-6",
                                ),
                                rx.el.div(
                                    profile_field(
                                        "Full Name", ProfileState.full_name, "full_name"
                                    ),
                                    profile_field(
                                        "Email Address",
                                        ProfileState.email,
                                        "email",
                                        "email",
                                    ),
                                    profile_field(
                                        "Phone Number",
                                        ProfileState.phone,
                                        "phone",
                                        "tel",
                                    ),
                                    profile_field(
                                        "Date of Birth", ProfileState.dob, "dob", "date"
                                    ),
                                    class_name="grid grid-cols-6 gap-6 mb-8",
                                ),
                                rx.el.h3(
                                    "Address Information",
                                    class_name="text-lg font-medium text-[#8B4513] mb-6",
                                ),
                                rx.el.div(
                                    profile_field(
                                        "Street Address",
                                        ProfileState.address,
                                        "address",
                                    ),
                                    profile_field("City", ProfileState.city, "city"),
                                    profile_field(
                                        "Postal Code",
                                        ProfileState.postal_code,
                                        "postal_code",
                                    ),
                                    class_name="grid grid-cols-6 gap-6",
                                ),
                                rx.el.div(
                                    rx.el.button(
                                        "Cancel",
                                        class_name="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#DAA520]",
                                    ),
                                    rx.el.button(
                                        "Save Changes",
                                        on_click=ProfileState.save_changes,
                                        class_name="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-[#8B4513] hover:bg-[#6d360f] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#8B4513]",
                                    ),
                                    class_name="flex justify-end mt-8",
                                ),
                                class_name="p-6 md:p-8 bg-white shadow rounded-lg border border-gray-200",
                            ),
                            class_name="md:col-span-3",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-4 gap-8",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
            class_name="flex-grow bg-gray-50",
        ),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )