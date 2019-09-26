from django.db import models

from django.contrib.auth.models import User
import threading



class ImageUpload(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='img/original/', null=True, blank=True)

    def __str__(self):
        if not self.author == None:
            return self.author.username
        return self.author

    def delete(self, *args, **kwargs):
        self.author.delete()
        self.image.delete()
        super().delete(*args, **kwargs)
