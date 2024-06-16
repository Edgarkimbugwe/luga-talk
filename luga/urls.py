from . import views
from django.urls import path
from .views import AboutView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]