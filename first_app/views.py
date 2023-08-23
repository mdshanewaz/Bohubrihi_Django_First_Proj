from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World!</h1> <a href='about/'>About</a> <a href='contact/'>Contact</a>")

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1> <a href='/'>Home</a> <a href='/about/'>About</a>")

def about(request):
    return HttpResponse("<h1>About Us</h1> <a href='/'>Home</a> <a href='/contact/'>Contact</a>")