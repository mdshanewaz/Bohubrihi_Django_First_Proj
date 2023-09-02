# from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form, name='form')
]
