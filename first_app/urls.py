# from django.conf.urls import url
from django.urls import path
from first_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_album/', views.album_form, name='album_form'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_login/', views.user_login, name='user_login'),   
    path('form/', views.form, name='form'),

    path('indexview/', views.IndexView.as_view(), name='indexview'),
    path('musicaian_details/<pk>/', views.MusiciandetailView.as_view(), name='musician_details'),
    path('test/', views.testview.as_view(), name='test'),
    path('add_new_singer/', views.AddMusician.as_view(), name='add_musician'),
    path('update_signer/<pk>/', views.MusicianupdateView.as_view(), name="update_signer"),
    path('delete_signer/<pk>/', views.MusiciandeleteView.as_view(), name='delete_signer'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
