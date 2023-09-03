from django import forms
from first_app import models

class user_form(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()
    