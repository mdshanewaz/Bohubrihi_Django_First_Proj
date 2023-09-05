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

    if request.method == "POST":
        
        new_form = forms.user_form(request.POST)
        diction.update({'test_form' : new_form})
        
        if new_form.is_valid():
            # user_name = new_form.cleaned_data['user_name']
            # user_email = new_form.cleaned_data['user_email']
            # user_dob = new_form.cleaned_data['user_dob']

            # diction.update({'user_name' : user_name})
            # diction.update({'user_email' : user_email})
            # diction.update({'user_dob' : user_dob})
            # diction.update({'boolean_field' : new_form.cleaned_data['boolean_chck']})
            #diction.update({'field_1' : new_form.cleaned_data['field_1']})
            diction.update({'field_1' : new_form.cleaned_data['field_2']})
            diction.update({'field' : 'fields match!'})
            diction.update({'form_submited' : 'Yes'})

    return render(request, 'first_app/form.html', context=diction)

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1>")