# posts/views.py
from django.core.files import File
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required

from .models import ImageUpload, ImageClone
from .forms import ImgForm
from django.utils.decorators import method_decorator


class HomePageView(ListView):
    model = ImageUpload
    template_name = 'home.html'


class CreateImgView(CreateView): # new
    model = ImageUpload
    form_class = ImgForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    @method_decorator(login_required(login_url='/admin'))
    def dispatch(self, *args, **kwargs):
        return super(CreateImgView, self).dispatch(*args, **kwargs)

    def clone_image(self, img_model):
        # Create a copy of the origina image
        picture_copy = ContentFile(img_model.image.read())
        new_picture_name = img_model.image.name.split("/")[-1]
        item = ImageClone.objects.create(author=self.request.user, image=File(picture_copy, new_picture_name))
        item.save()

    def form_valid(self, form):
        img_model = form.save(commit=False)
        img_model.author = self.request.user
        img_model.save()
        self.clone_image(img_model)
        return super().form_valid(form)