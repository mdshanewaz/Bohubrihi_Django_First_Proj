from django import forms
from django.contrib.auth.models import User
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type' : 'date'}))
    class Meta:
        model = models.Album
        fields = '__all__'

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.Userinfo
        fields = ('facebook_id', 'profile_pic')
