from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, Photo
from .forms import PhotoUploadForm

def album_list(request):
    albums = Album.objects.filter(user=request.user)
    album_data = []
    for album in albums:
        random_photo = album.get_random_photo()
        album_data.append({
            'album': album,
            'random_photo': random_photo
        })
    return render(request, 'album_list.html', {'album_data': album_data})

def photo_list(request, album_id):
    photos = Photo.objects.filter(album=album_id)
    return render(request, 'photo_list.html', {'photos': photos})

@login_required
def upload_photo(request, album_id):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoUploadForm()
    return render(request, 'upload_photo.html', {'form': form})
