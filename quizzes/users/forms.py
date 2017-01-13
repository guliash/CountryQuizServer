from django import forms
from .validators import *

class SignupForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),
        validators=[validate_password_length])
