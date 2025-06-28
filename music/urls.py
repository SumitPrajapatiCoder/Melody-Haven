from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_list, name='music_list'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout-home/', views.logout_then_home, name='logout_home'),
    path('upload/', views.upload_song, name='upload_song'),
    path('delete/', views.delete_song, name='delete_song'),
    path('users/', views.user_list, name='user_list'), 
    path('edit/<int:song_id>/', views.edit_song, name='edit_song'),

]
