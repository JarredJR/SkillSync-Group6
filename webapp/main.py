import flet as ft
from webapp.pages.login import LoginPage

def main(page: ft.Page):
    page.title = "SkillSync"
    page.scroll = "auto"

    login = LoginPage()
    page.add(login)
