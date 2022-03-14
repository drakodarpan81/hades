from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myfirstview(request):
    return HttpResponse('Hola está es mi primera URL')


def mysecondview(request):
    return HttpResponse('Hola está es mi primera URL')
