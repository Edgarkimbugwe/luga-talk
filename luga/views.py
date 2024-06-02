from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_luga(request):
    return HttpResponse("Hello, Luganda!")

def about(request):
    return HttpResponse("About Us!")