# posts/views.py
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy
from .models import ImageUpload
from .forms import ImgForm

class HomePageView(ListView):
    model = ImageUpload
    template_name = 'home.html'

class CreateImgView(CreateView): # new
    model = ImageUpload
    form_class = ImgForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        img_model = form.save(commit=False)
        img_model.author = self.request.user
        # app_model.user = User.objects.get(user=self.request.user) # Or explicit model 
        img_model.save()
        return super().form_valid(form)