from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)
    

def item(request):
    return HttpResponse("This is an Item View")