from . import views
from django.urls import path
from .views import AboutView, create_blogpost
# from .views import test_500


urlpatterns = [
    # path('test-500/', test_500),
    path('', views.PostList.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('create/', create_blogpost, name='create-blogpost'),
    path('like/<int:post_id>/', views.like_blogpost, name='like_blogpost'),
    path('remove_favorite/<int:post_id>/',
         views.remove_favorite, name='remove_favorite'),
    path('my-blogposts/', views.user_blogposts, name='user_blogposts'),
    path('<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit/', views.blogpost_edit, name='blogpost_edit'),
    path('<slug:slug>/delete/',
         views.blogpost_delete, name='blogpost_delete'),
]
