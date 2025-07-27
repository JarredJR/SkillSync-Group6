import flet as ft
import json
import os

SERVICE_CATEGORIES = [
    "Mechanic", "Electrician", "Plumber", "HVAC Technician", "Carpenter",
    "Mason/Tiler", "Painter", "Welder", "Locksmith", "General Contractor",
    "Roofer", "Glass Installer", "Landscaper/Gardener", "Pest Control Specialist",
    "Handyman", "Appliance Repair", "Gadget Repair", "IT Technician",
    "CCTV Installer", "Smart Home Installer", "House Cleaner", "Car Wash / Detailing",
    "Laundry / Ironing Services", "Sofa / Carpet Cleaning", "Pet Groomer",
    "Tailor", "Massage Therapist", "Barber/Hairdresser", "Event Organizer",
    "Caregiver"
]

def service_form_view(page: ft.Page):

    category_dropdown = ft.Dropdown(
        label="Select service category",
        options=[ft.dropdown.Option(c) for c in SERVICE_CATEGORIES],
        width=400
    )

    description_field = ft.TextField(
        label="Describe your service request...",
        multiline=True,
        width=400
    )

    location_field = ft.TextField(
        label="Enter your location manually",
        width=400
    )

    def submit_request(e):
        user = page.session.get("user", {})
        if not user:
            page.snack_bar = ft.SnackBar(ft.Text("Please log in first."))
            page.snack_bar.open = True
            page.update()
            return

        request_data = {
            "username": user.get("username"),
            "email": user.get("email"),
            "category": category_dropdown.value,
            "description": description_field.value,
            "location": location_field.value
        }
        if os.path.exists("data/requests.json"):
            with open("data/requests.json", "r") as f:
                all_requests = json.load(f)
        else:
            all_requests = []

        all_requests.append(request_data)

        with open("data/requests.json", "w") as f:
            json.dump(all_requests, f, indent=4)

        page.snack_bar = ft.SnackBar(ft.Text("Service request submitted!"))
        page.snack_bar.open = True
        page.update()

        category_dropdown.value = None
        description_field.value = ""
        location_field.value = ""
        page.update()

    return ft.View(
        "/service_form",
        controls=[
            ft.Text("Post a Service Request", size=30, weight="bold"),
            category_dropdown,
            description_field,
            location_field,
            ft.ElevatedButton("Submit Request", on_click=submit_request),
            ft.ElevatedButton("Back to Dashboard", on_click=lambda e: page.go("/dashboard"))
        ]
    )
