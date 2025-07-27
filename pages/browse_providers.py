import flet as ft
import json
import os
from components.topbar import topbar

def browse_providers_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/login")
        return

    result_column = ft.Column(spacing=15, expand=True)

    category_dropdown = ft.Dropdown(
        label="Filter by Category",
        options=[
            ft.dropdown.Option("Mechanic"),
            ft.dropdown.Option("Electrician"),
            ft.dropdown.Option("Plumber"),
            ft.dropdown.Option("HVAC Technician"),
            ft.dropdown.Option("Carpenter"),
            ft.dropdown.Option("Painter"),
            ft.dropdown.Option("IT Technician"),
            ft.dropdown.Option("Pet Groomer"),
            ft.dropdown.Option("House Cleaner"),
            ft.dropdown.Option("Tailor"),
            ft.dropdown.Option("Massage Therapist"),
            ft.dropdown.Option("Barber/Hairdresser"),
            ft.dropdown.Option("Event Organizer"),
            ft.dropdown.Option("Caregiver"),
        ],
        width=300,
    )

    search_field = ft.TextField(label="Search by Name", width=300)

    def start_chat_with(email):
        page.session.set("chat_with", email)
        page.go("/chat")

    def load_providers():
        result_column.controls.clear()
        if not os.path.exists("data/providers.json"):
            result_column.controls.append(ft.Text("No providers found."))
            page.update()
            return
        with open("data/providers.json", "r") as f:
            try:
                providers = json.load(f)
            except json.JSONDecodeError:
                providers = []
        filtered = []
        for p in providers:
            if category_dropdown.value and p.get("category") != category_dropdown.value:
                continue
            if search_field.value and search_field.value.lower() not in p.get("username", "").lower():
                continue
            filtered.append(p)
        if not filtered:
            result_column.controls.append(ft.Text("No matching providers found."))
        else:
            for p in filtered:
                result_column.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(f"Name: {p.get('username', 'N/A')}", weight="bold"),
                                    ft.Text(f"Category: {p.get('category', 'N/A')}"),
                                    ft.Text(f"Overview: {p.get('overview', 'No overview provided')}"),
                                    ft.Text(f"Experience: {p.get('experience', 'N/A')}"),
                                    ft.Row([
                                        ft.ElevatedButton("Message", on_click=lambda e, email=p.get("email"): start_chat_with(email))
                                    ])
                                ],
                                spacing=5
                            ),
                            padding=10
                        )
                    )
                )
        page.update()

    def on_filter_change(e):
        load_providers()

    category_dropdown.on_change = on_filter_change
    search_field.on_change = on_filter_change
    load_providers()

    return ft.View(
        "/browse_providers",
        controls=[
            topbar(page, "Browse Providers"),
            ft.Row([category_dropdown, search_field], spacing=20),
            result_column
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
