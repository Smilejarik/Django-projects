from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Aske is cool programmer!")
# Create your views here.


def masina():
    return HttpResponse("co sie stalo?")
