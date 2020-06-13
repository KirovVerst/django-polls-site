from django.contrib.auth import forms as auth_forms

from polls_service.forms import BaseForm


class UserLoginForm(BaseForm, auth_forms.AuthenticationForm):
    ...


class UserRegistrationForm(BaseForm, auth_forms.UserCreationForm):
    ...


class PasswordChangeForm(BaseForm, auth_forms.PasswordChangeForm):
    ...
