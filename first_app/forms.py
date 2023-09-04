from django import forms
from first_app import models

class user_form(forms.Form):
    user_name = forms.CharField(required=False, label='Name', initial='Sawon')

    user_email = forms.EmailField(label='Email', widget= forms.TextInput(attrs={
        'placeholder' : 'Enter a valid email',
        'style' : 'width: 300px',
    }))

    user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput(attrs={
        'type' : 'date',
    }))
