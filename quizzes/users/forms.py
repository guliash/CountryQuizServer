from django import forms
from django.contrib.auth.password_validation import validate_password

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput(),
                               validators = [validate_password])

class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput(),)
