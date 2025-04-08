from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.title}"
    def get_random_photo(self):
        photos = self.photo_set.all()
        if photos.exists():
            return random.choice(photos)
        return None


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Открываем изображение и сохраняем размеры
        img = Image.open(self.image.path)
        self.width, self.height = img.size
        # Обновляем объект без пересохранения файла
        Photo.objects.filter(pk=self.pk).update(width=self.width, height=self.height)

    def __str__(self):
        return f"{self.album.title} - {self.image.name}"
