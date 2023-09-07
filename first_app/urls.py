# from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_album/', views.album_form, name="album_form"),
    path('add_musician/', views.musician_form, name="musician_form"),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('form/', views.form, name='form'),
]
