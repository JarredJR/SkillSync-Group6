import flet as ft
from components.topbar import topbar

def role_question_view(page: ft.Page):
    def handle_yes(e):
        page.go("/provider_setup")
    def handle_no(e):
        page.go("/request_service")

    return ft.View(
        "/role_question",
        controls=[
            topbar(page, "Choose Your Role"),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Can you provide a service?", size=24, weight="bold"),
                        ft.Row(
                            [
                                ft.ElevatedButton("Yes", on_click=handle_yes, width=150),
                                ft.ElevatedButton("No", on_click=handle_no, width=150),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                        ),
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=30,
                alignment=ft.alignment.center,
            ),
        ],
    )
