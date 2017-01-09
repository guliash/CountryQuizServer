from django import forms

class CreateForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
