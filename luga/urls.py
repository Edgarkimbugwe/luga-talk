from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_luga, name='luga-home'),
    path('about/', views.about, name='luga-about'),
]