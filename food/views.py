from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
    

def work(request):
    return HttpResponse("This is the work page")