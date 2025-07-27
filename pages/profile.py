import flet as ft

def profile_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/")
        return

    welcome_text = ft.Text(f"Welcome, {user['username']}!", size=24, weight="bold")
    question = ft.Text("Can you provide a service?", size=18)

    yes_btn = ft.ElevatedButton("Yes", on_click=lambda e: page.go("/provider_setup"))
    no_btn = ft.ElevatedButton("No", on_click=lambda e: page.go("/request_service"))

    return ft.View(
        "/profile",
        controls=[
            ft.Container(
                content=ft.Column([
                    welcome_text,
                    ft.Divider(),
                    question,
                    ft.Row([yes_btn, no_btn], alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=50,
                width=600
            )
        ]
    )
