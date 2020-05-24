from django.contrib.auth import forms as auth_forms

from polls_service.forms import BaseForm


class UserLoginForm(BaseForm, auth_forms.AuthenticationForm):
    ...


class PasswordChangeForm(BaseForm, auth_forms.PasswordChangeForm):
    ...
