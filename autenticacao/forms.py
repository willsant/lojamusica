from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput
from django.forms.widgets import TextInput

class AuthenticationFormCustomizado(AuthenticationForm):

    username = forms.CharField(
        error_messages={'required': 'Campo de preenchimento obrigatório.',},
        max_length=40,
        widget=TextInput(attrs={'autofocus': True,'class': 'form-control form-control-sm'}),
        required=True)

    password = forms.CharField(
        error_messages={'required': 'Campo de preenchimento obrigatório.',},
        max_length=255,
        widget=PasswordInput(attrs={'class': 'form-control form-control-sm'}),
        required = True)

    error_messages = {
        'invalid_login': "Login invalido.",
        'inactive': "Conta inativa.",
    }