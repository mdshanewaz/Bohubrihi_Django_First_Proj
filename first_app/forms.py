from django import forms
#from first_app.models import Album, Musician #Album
from first_app import models #models.Album
from django.core import validators


class MusicianForm(forms.ModelForm):
    
    class Meta:
        model = models.Musician
        fields = '__all__'
        #exclude = ['first_name']
        #fields = ('first_name', 'last_name',)

def even_or_odd(value):
    if value%2 == 1:
        raise forms.ValidationError("Please Insert an Even Number!")

class user_form(forms.Form):
    # user_name = forms.CharField(required=False, label='Name', initial='Sawon')

    # user_email = forms.EmailField(label='Email', widget= forms.TextInput(attrs={
    #     'placeholder' : 'Enter a valid email',
    #     'style' : 'width: 250px',
    # }))

    # user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput(attrs={
    #     'type' : 'date',
    # }))

    # boolean_chck = forms.BooleanField(required=False)

    #field_1 = forms.CharField(max_length=15, min_length=5)

    #choices = (('', 'SELECT OPTION'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    # field_1 = forms.ChoiceField(choices=choices, required=False)

    choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field_1 = forms.ChoiceField(choices=choices, widget=forms.RadioSelect())

    #field_1 = forms.MultipleChoiceField(choices=choices, required=False, widget=forms.CheckboxSelectMultiple())

    field_1 = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)], required=False)
    field_2 = forms.IntegerField(validators=[validators.MaxValueValidator(15), validators.MinValueValidator(5)], required=False)
    field_3 = forms.IntegerField(validators=[even_or_odd], required=False)

    user_email1 = forms.EmailField()
    user_email2 = forms.EmailField()

    def clean(self):
        all_cleaned_data = super().clean() 
        user_email1 = all_cleaned_data['user_email1']
        user_email2 = all_cleaned_data['user_email2']

        if user_email1 != user_email2:
            raise forms.ValidationError("Fields don't match!")