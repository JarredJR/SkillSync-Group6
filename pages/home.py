import flet as ft

def home_view(page: ft.Page, current_user):
    def handle_provider_choice(choice):
        if choice == "yes":
            page.dialog = ft.AlertDialog(title=ft.Text("Provider setup coming next..."))
            page.dialog.open = True
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("You can now browse or request services."))
            page.dialog.open = True
        page.update()

    return ft.View(
        route="/home",
        controls=[
            ft.Text(f"Welcome, {current_user['username']}!", size=25, weight="bold"),
            ft.Text("Can you provide any services?"),
            ft.Row([
                ft.ElevatedButton("Yes", on_click=lambda e: handle_provider_choice("yes")),
                ft.ElevatedButton("No", on_click=lambda e: handle_provider_choice("no")),
            ])
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
