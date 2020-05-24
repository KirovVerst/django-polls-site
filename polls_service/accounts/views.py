from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .forms import UserLoginForm


class LoginView(auth_views.LoginView):
    authentication_form = UserLoginForm
    template_name = "accounts/login.html"


class LogoutView(auth_views.LogoutView):
    ...


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:password_change_done")


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"
