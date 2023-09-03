from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.

def home(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'text_1' : 'I am a text from views.py',
        'musician' : musician_list,
    }
    return render(request, 'first_app/index.html', context=diction)

def form(request):
    new_form = forms.user_form()
    diction = {
        'test_form' : new_form,
        'heading_1' : 'This form is created using django Library',
    }
    return render(request, 'first_app/form.html', context=diction)

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1>")