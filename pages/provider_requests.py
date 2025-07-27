import flet as ft
import json
import os
from components.topbar import topbar

def provider_requests_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/login")
        return ft.View("/login", [])

    request_list = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    def load_requests():
        request_list.controls.clear()
        requests_path = "data/requests.json"
        if not os.path.exists(requests_path):
            request_list.controls.append(ft.Text("No service requests available."))
        else:
            with open(requests_path, "r") as f:
                try:
                    requests = json.load(f)
                except json.JSONDecodeError:
                    requests = []

            if not requests:
                request_list.controls.append(ft.Text("No service requests available."))
            else:
                for req in requests:
                    request_list.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Text(f"Service: {req.get('category', 'N/A')}", weight="bold"),
                                    ft.Text(f"Description: {req.get('description', '')}"),
                                    ft.Text(f"Location: {req.get('location', '')}"),
                                    ft.ElevatedButton("Message", on_click=lambda e, r=req: open_chat(r))
                                ]),
                                padding=10
                            )
                        )
                    )
        page.update()

    def open_chat(request):
        page.session.set("chat_with", request.get("username", "Unknown"))
        page.go("/chat")

    load_requests()

    return ft.View(
        "/provider_requests",
        controls=[
            topbar(page, "Service Requests"),
            ft.Container(content=request_list, expand=True),
            ft.ElevatedButton("Back to Dashboard", on_click=lambda e: page.go("/dashboard"))
        ]
    )
