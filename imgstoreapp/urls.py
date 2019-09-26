# posts/urls.py
from django.urls import path

from .views import HomePageView, CreateImgView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreateImgView.as_view(), name='add_post'),
]