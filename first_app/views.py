from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album, Userinfo
from first_app import forms
from first_app.forms import UserForm, UserInfoForm
from django.db.models import Avg, Max, Min
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

# def home(request):
#     musician_list = Musician.objects.order_by('first_name')
#     diction = {
#         'text_1' : 'I am a text from views.py',
#         'musician' : musician_list,
#         # 'sample_txt' : Album.objects.get(pk=1).release_date,

#         'sample_txt' : 'Sample text from view',
#     }
#     return render(request, 'first_app/index.html', context=diction)

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user_form.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            
            user_info.save()
            registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    diction = {
        'title' : 'Register',
        'user_form' : user_form,
        'user_info_form' : user_info_form,
        'registered' : registered,
    }

    return render(request, 'first_app/register.html', context=diction)

def login_view(request):
    diction = {
        'title' : 'Login',
    }
    return render(request, 'first_app/login.html', context=diction)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:index'))
                #return render(request, 'first_app/index.html', context={})
                #return index(request)
            else:
                return HttpResponse('Account is not active!')
        else:
            return HttpResponse("Login details are worng!")
    else:
        #return render(request, 'first_app/login.html', context={"title":"Login"})
        return HttpResponseRedirect(reverse('first_app:login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:index'))

def form(request):

    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)

    diction = {
        'test_form' : new_form,
        #'heading_1' : 'This form is created using django Library',
        'heading_1' : 'Add New Musician',
        'title' : 'Forms'
    }

    # if request.method == "POST":
        
    #     new_form = forms.user_form(request.POST)
    #     diction.update({'test_form' : new_form})
        
        # if new_form.is_valid():
            # user_name = new_form.cleaned_data['user_name']
            # user_email = new_form.cleaned_data['user_email']
            # user_dob = new_form.cleaned_data['user_dob']

            # diction.update({'user_name' : user_name})
            # diction.update({'user_email' : user_email})
            # diction.update({'user_dob' : user_dob})
            # diction.update({'boolean_field' : new_form.cleaned_data['boolean_chck']})
            #diction.update({'field_1' : new_form.cleaned_data['field_1']})
            # diction.update({'field_1' : new_form.cleaned_data['field_2']})
            # diction.update({'field' : 'fields match!'})
            # diction.update({'form_submited' : 'Yes'})

    return render(request, 'first_app/form.html', context=diction)

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'title' : 'Home Page',
        'listofmusician' : musician_list,
    }

    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = Userinfo.objects.get(user__pk=user_id) # Here '__' is the where condition of sql

        diction.update(
            {
             'user_basic_info': user_basic_info,
             'user_more_info' : user_more_info,
             }
        )

    print(diction)

    return render(request, 'first_app/index.html', context= diction)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist = artist_id).order_by('name', 'release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    diction = {
        'title' : 'List of Albums',
        'artist_info' : artist_info,
        'album_info' : album_list,
        'artist_rating' : artist_rating,
    }
    return render(request, 'first_app/album_list.html', context=diction)

def musician_list(request):
    diction = {
        'title' : 'List of Musician',
    }
    return render(request, 'first_app/musician_list.html', context=diction) 

def album_form(request):
    album_form = forms.AlbumForm
    diction = {
        'title' : 'Add Album',
        'form' : album_form
    }
    if request.method == "POST":
        album_form = forms.AlbumForm(request.POST)

        if album_form.is_valid():
            album_form.save( commit=True)
            return index(request)

    return render(request, 'first_app/album_form.html', context=diction)

def musician_form(request):
    musician_form = forms.MusicianForm
    diction = {
        'title' : "Add Musician",
        'form' : musician_form,
    }

    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST)

        if musician_form.is_valid():
            musician_form.save(commit=True)
            return index(request)

    return render(request, 'first_app/musician_form.html', context=diction)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == "POST":
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)

    diction = {
        'edit_form' : form,
        'title' : "Edit Musician",
    }
    return render(request, 'first_app/edit_artist.html', context=diction)

def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction = {}

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated'})

    diction.update({
        'edit_form' : form,
        'title' : "Edit Album",
        'album_id' : album_id
    })

    return render(request, 'first_app/edit_album.html', context=diction)

def delete_album(request, album_id):
    album_info = Album.objects.get(pk=album_id).delete()
    
    diction = {
        'title' : "Delete Album",
        'delete_success' : 'Album is deleted'
           }
    return render(request, 'first_app/delete.html', context=diction)

def delete_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id).delete()

    diction = {
        'title' : "Delete Musician",
        'delete_success' : 'Musician is deleted'
    }

    return render(request, 'first_app/delete.html', context=diction)

