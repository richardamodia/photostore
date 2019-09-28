from django.db import models

from django.contrib.auth.models import User
import threading



class ImageUpload(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/original/')

    def __str__(self):
        if not self.author == None:
            return self.author.username
        return self.author


class ImageClone(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='img/clone/', null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    crop_to_fit = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        img_str = "%s - %s" % (self.author.username,self.image.name)
        return img_str