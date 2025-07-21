import flet as ft

def login_view(page: ft.Page):
    username = ft.TextField(label="Username", autofocus=True)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    result_text = ft.Text(value="", color="red")  # Use string color here

    def login_clicked(e):
        print("Login clicked")
        result_text.value = "Login clicked"
        page.update()

    def go_signup(e):
        page.go("/signup")

    return ft.View(
        "/",
        controls=[
            ft.Text("Login", size=30, weight="bold"),
            username,
            password,
            ft.ElevatedButton("Login", on_click=login_clicked),
            result_text,
            ft.TextButton("Don't have an account? Sign up here.", on_click=go_signup),
        ]
    )
