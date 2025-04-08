from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('albums', views.album_list, name='album_list'),
    path('albums/<str:album_id>', views.photo_list, name='photo_list'),
    path('albums/<str:album_id>/upload', views.upload_photo, name='upload_photo'),
]
