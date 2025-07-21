import flet as ft

def signup_view(page: ft.Page):
    email = ft.TextField(label="Email", autofocus=True)
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    result_text = ft.Text(value="", color="red")

    def signup_clicked(e):
        print("Signup clicked")
        result_text.value = "Signup clicked"
        page.update()

    def go_login(e):
        page.go("/")

    return ft.View(
        "/signup",
        controls=[
            ft.Text("Signup", size=30, weight="bold"),
            email,
            username,
            password,
            ft.ElevatedButton("Signup", on_click=signup_clicked),
            result_text,
            ft.TextButton("Already have an account? Login here.", on_click=go_login),
        ]
    )
