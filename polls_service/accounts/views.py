from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import PasswordChangeForm
from .forms import UserLoginForm
from .forms import UserRegistrationForm
from polls_service.views import BaseView


class LoginView(BaseView, auth_views.LoginView):
    authentication_form = UserLoginForm
    template_name = "accounts/login.html"


class RegistrationView(BaseView, FormView):
    form_class = UserRegistrationForm
    template_name = "accounts/registration.html"


class LogoutView(auth_views.LogoutView):
    ...


class PasswordChangeView(BaseView, auth_views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:password_change_done")
    form_class = PasswordChangeForm


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"
