from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/specialist", views.register_specialist, name="register_specialist"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("type/", views.register_type, name="register_type"),
    path("register/member", views.register_member, name="register_member"),
]