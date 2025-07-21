import flet as ft
from pages.login import login_view
from pages.signup import signup_view

def main(page: ft.Page):
    page.title = "SkillSync"
    
    def route_change(route):
        page.views.clear()
        if page.route == "/signup":
            page.views.append(signup_view(page))
        else:
            page.views.append(login_view(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
