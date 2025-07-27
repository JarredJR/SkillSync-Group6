import flet as ft

def dashboard_view(page: ft.Page):
    user = page.session.get("user")
    if not user:
        page.go("/login")
        return ft.View("/login", [])

    def handle_provider(e):
        page.go("/provider_setup")

    def handle_seeker(e):
        page.go("/request_service")

    return ft.View(
        "/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Dashboard - Welcome, {user.get('username', 'User')}"),
                center_title=True,
                actions=[
                    ft.TextButton("Browse Providers", on_click=lambda e: page.go("/browse_providers")),
                    ft.TextButton("Service Requests", on_click=lambda e: page.go("/provider_requests")),
                    ft.TextButton("Logout", on_click=lambda e: logout(page))
                ]
            ),
            ft.Column(
                [
                    ft.Text("What would you like to do?", size=24, weight="bold"),
                    ft.Row(
                        [
                            ft.ElevatedButton("I am a Service Provider", on_click=handle_provider),
                            ft.ElevatedButton("I need a Service", on_click=handle_seeker)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ]
    )

def logout(page: ft.Page):
    page.session.set("user", None)
    page.go("/login")
