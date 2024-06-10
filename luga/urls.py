from . import views
from django.urls import path
from .views import AboutView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),
]