import flet as ft
import sys, os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller bundle"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

from pages.login import login_view
from pages.signup import signup_view
from pages.role_question import role_question_view
from pages.provider_setup import provider_setup_view
from pages.request_service import request_service_view
from pages.browse_providers import browse_providers_view
from pages.dashboard import dashboard_view
from pages.provider_requests import provider_requests_view
from pages.chat import chat_view  
from pages.messages import messages_view  

def main(page: ft.Page):
    page.title = "SkillSync"
    if not page.session.get("user"):
        page.session.set("user", None)

    def route_change(route):
        page.views.clear()
        current_user = page.session.get("user")

        protected_routes = [
            "/dashboard", "/role_question", "/provider_setup",
            "/request_service", "/browse_providers", "/provider_requests", "/chat", "/messages"
        ]
        if not current_user and page.route in protected_routes:
            page.go("/login")
            return

        if page.route == "/signup":
            page.views.append(signup_view(page))
        elif page.route == "/dashboard":
            page.views.append(dashboard_view(page))
        elif page.route == "/role_question":
            page.views.append(role_question_view(page))
        elif page.route == "/provider_setup":
            page.views.append(provider_setup_view(page))
        elif page.route == "/request_service":
            page.views.append(request_service_view(page))
        elif page.route == "/browse_providers":
            page.views.append(browse_providers_view(page))
        elif page.route == "/provider_requests":
            page.views.append(provider_requests_view(page))
        elif page.route == "/chat":
            page.views.append(chat_view(page))
        elif page.route == "/messages":
            page.views.append(messages_view(page))
        else:
            page.views.append(login_view(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route if page.views else "/login")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
