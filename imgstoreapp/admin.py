from django.contrib import admin
from imgstoreapp.models import ImageUpload

class ImageAdmin(admin.ModelAdmin):
    fields = ('author', 'image')

admin.site.register(ImageUpload, ImageAdmin)