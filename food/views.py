from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
    

def item(request):
    return HttpResponse("This is an Item View")