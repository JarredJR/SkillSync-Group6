import flet as ft

def topbar(page: ft.Page, title: str):
    def go_dashboard(e):
        page.go("/dashboard")

    def go_messages(e):
        page.go("/messages")

    def logout(e):
        page.session.set("user", None)
        page.go("/login")

    return ft.AppBar(
        title=ft.Text(title, size=20, weight="bold"),
        bgcolor="#E0E0E0",
        actions=[
            ft.IconButton(icon="home", tooltip="Go to Dashboard", icon_size=32, on_click=go_dashboard),
            ft.IconButton(icon="chat", tooltip="Messages", icon_size=32, on_click=go_messages),
            ft.IconButton(icon="logout", tooltip="Logout", icon_size=32, on_click=logout),
        ]
    )
