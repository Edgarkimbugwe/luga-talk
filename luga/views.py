from django.shortcuts import render
from django.views import generic
from .models import BlogPost

# Create your views here.
class PostList(generic.ListView):
    queryset = BlogPost.objects..filter(status=1)
    template_name = "blogpost_list.html"