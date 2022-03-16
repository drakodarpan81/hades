from django.shortcuts import render
from django.http import HttpResponse

from .models import Category

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def Index(request):
    return render(request, 'index.html')