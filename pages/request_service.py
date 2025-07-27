import flet as ft
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUESTS_FILE = os.path.join(BASE_DIR, "data", "service_requests.json")

def request_service_view(page: ft.Page):
    service_category_dropdown = ft.Dropdown(
        label="Service Category",
        options=[
            ft.dropdown.Option("Mechanic"),
            ft.dropdown.Option("Electrician"),
            ft.dropdown.Option("Plumber"),
            ft.dropdown.Option("HVAC Technician"),
            ft.dropdown.Option("Carpenter"),
            ft.dropdown.Option("Mason/Tiler"),
            ft.dropdown.Option("Painter"),
            ft.dropdown.Option("Welder"),
            ft.dropdown.Option("Locksmith"),
            ft.dropdown.Option("General Contractor"),
            ft.dropdown.Option("Roofer"),
            ft.dropdown.Option("Glass Installer"),
            ft.dropdown.Option("Landscaper/Gardener"),
            ft.dropdown.Option("Pest Control Specialist"),
            ft.dropdown.Option("Handyman"),
            ft.dropdown.Option("Appliance Repair"),
            ft.dropdown.Option("Gadget Repair"),
            ft.dropdown.Option("IT Technician"),
            ft.dropdown.Option("CCTV Installer"),
            ft.dropdown.Option("Smart Home Installer"),
            ft.dropdown.Option("House Cleaner"),
            ft.dropdown.Option("Car Wash / Detailing"),
            ft.dropdown.Option("Laundry / Ironing Services"),
            ft.dropdown.Option("Sofa / Carpet Cleaning"),
            ft.dropdown.Option("Pet Groomer"),
            ft.dropdown.Option("Tailor"),
            ft.dropdown.Option("Massage Therapist"),
            ft.dropdown.Option("Barber/Hairdresser"),
            ft.dropdown.Option("Event Organizer"),
            ft.dropdown.Option("Caregiver"),
        ],
        width=400,
    )

    service_description = ft.TextField(label="Service Description", multiline=True, width=400)
    location = ft.TextField(label="Your Location", width=400)
    confirmation_text = ft.Text(value="", color="green")

    def save_request(e):
        user = page.session.get("user")
        if not user:
            user = {}

        request_data = {
            "username": user.get("username", "Anonymous"),
            "category": service_category_dropdown.value,
            "description": service_description.value,
            "location": location.value,
        }

        if not os.path.exists(REQUESTS_FILE):
            with open(REQUESTS_FILE, "w") as f:
                json.dump([], f)

        with open(REQUESTS_FILE, "r+") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

            data.append(request_data)
            f.seek(0)
            json.dump(data, f, indent=4)

        confirmation_text.value = "Request submitted successfully!"
        page.update()

    return ft.View(
        "/request-service",
        controls=[
            ft.Text("Request a Service", size=24, weight="bold"),
            service_category_dropdown,
            service_description,
            location,
            ft.ElevatedButton("Submit Request", on_click=save_request),
            confirmation_text,
            ft.TextButton("Back", on_click=lambda e: page.go("/dashboard"))
        ],
        scroll=ft.ScrollMode.AUTO
    )
