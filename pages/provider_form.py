import flet as ft
import json
import os
from utils.path_helper import resource_path

providers_file = resource_path("data/providers.json")

def provider_form_view(page: ft.Page):
    category_dropdown = ft.Dropdown(
        label="Select Service Category",
        options=[
            ft.dropdown.Option("Mechanic"),
            ft.dropdown.Option("Electrician"),
            ft.dropdown.Option("Plumber"),
            ft.dropdown.Option("Carpenter"),
            ft.dropdown.Option("House Cleaner"),
            ft.dropdown.Option("Massage Therapist"),
            ft.dropdown.Option("Hairdresser"),
        ],
        width=300
    )

    overview_field = ft.TextField(label="Overview (e.g. skills, tools, etc.)", multiline=True, width=400)
    experience_field = ft.TextField(label="Years/Months of Experience", width=200)

    status_text = ft.Text("")

    def save_provider_data(e):
        if not category_dropdown.value or not overview_field.value or not experience_field.value:
            status_text.value = "Please fill out all fields."
            page.update()
            return

        provider = {
            "email": page.session.get("user", {}).get("email", "unknown"),
            "category": category_dropdown.value,
            "overview": overview_field.value,
            "experience": experience_field.value
        }

        if os.path.exists(providers_file):
            with open(providers_file, "r") as f:
                try:
                    providers = json.load(f)
                except json.JSONDecodeError:
                    providers = []
        else:
            providers = []

        providers.append(provider)
        os.makedirs(os.path.dirname(providers_file), exist_ok=True)
        with open(providers_file, "w") as f:
            json.dump(providers, f, indent=2)

        status_text.value = "Provider info saved!"
        category_dropdown.value = None
        overview_field.value = ""
        experience_field.value = ""
        page.update()

    def go_back(e):
        page.go("/role-question")

    return ft.View(
        "/provider-form",
        controls=[
            ft.Text("Service Provider Form", size=24, weight="bold"),
            category_dropdown,
            overview_field,
            experience_field,
            ft.Row([
                ft.ElevatedButton("Save", on_click=save_provider_data),
                ft.TextButton("Back", on_click=go_back)
            ]),
            status_text
        ],
        scroll=ft.ScrollMode.AUTO
    )
