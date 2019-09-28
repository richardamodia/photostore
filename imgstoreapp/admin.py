from django.contrib import admin
from imgstoreapp.models import ImageUpload, ImageClone

class ImageAdmin(admin.ModelAdmin):
    fields = ('author', 'image')

class CloneAdmin(admin.ModelAdmin):
    fields = ('author', 'image', 'crop_to_fit', 'width', 'height')

admin.site.register(ImageUpload, ImageAdmin)
admin.site.register(ImageClone, CloneAdmin)