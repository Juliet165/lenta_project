from django.contrib import admin
from .models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description')
    search_fields = ('title', 'user__username')
    list_filter = ('user',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('album', 'image', 'uploaded_at')
    search_fields = ('album__title', 'album__user__username')
    list_filter = ('album', 'uploaded_at')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)