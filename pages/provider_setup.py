import flet as ft
import json
import os
from utils.path_helper import resource_path
from components.topbar import topbar

def provider_setup_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/login")
        return ft.View("/login", [])

    SERVICE_CATEGORIES = [
        "Mechanic", "Electrician", "Plumber", "HVAC Technician", "Carpenter",
        "Mason/Tiler", "Painter", "Welder", "Locksmith", "General Contractor",
        "Roofer", "Glass Installer", "Landscaper/Gardener", "Pest Control Specialist",
        "Handyman", "Appliance Repair", "Gadget Repair", "IT Technician",
        "CCTV Installer", "Smart Home Installer", "House Cleaner / Deep Cleaning",
        "Car Wash / Detailing", "Laundry / Ironing Services", "Sofa / Carpet Cleaning",
        "Pet Groomer", "Tailor", "Massage Therapist", "Barber/Hairdresser",
        "Event Organizer", "Caregiver"
    ]

    category_dropdown = ft.Dropdown(
        label="Select Service Category",
        options=[ft.dropdown.Option(c) for c in SERVICE_CATEGORIES],
        width=400
    )
    overview = ft.TextField(label="Overview of Expertise", multiline=True, width=400)
    experience = ft.TextField(label="Years of Experience", width=400)
    status = ft.Text(color="green")

    def save_provider_profile(e):
        provider_data = {
            "email": user.get("email"),
            "username": user.get("username"),
            "category": category_dropdown.value,
            "overview": overview.value,
            "experience": experience.value
        }

        providers_path = resource_path("providers.json")
        if os.path.exists(providers_path):
            try:
                with open(providers_path, "r") as f:
                    providers = json.load(f)
            except json.JSONDecodeError:
                providers = []
        else:
            providers = []

        providers.append(provider_data)
        with open(providers_path, "w") as f:
            json.dump(providers, f, indent=4)

        status.value = "Profile saved!"
        page.update()
        page.go("/provider_requests")

    return ft.View(
        "/provider_setup",
        controls=[
            topbar(page, "Provider Profile Setup"),
            ft.Column(
                [
                    ft.Text(f"Hi {user['username']}, setup your provider profile", size=20, weight="bold"),
                    category_dropdown,
                    overview,
                    experience,
                    ft.ElevatedButton("Save", on_click=save_provider_profile, width=200),
                    status
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )
