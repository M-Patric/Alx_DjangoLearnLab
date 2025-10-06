from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views   # <--- import the whole views module

urlpatterns = [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),


    # Authentication URLs
    path("register/", views.register, name="register"),  # <--- now it's views.register
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
