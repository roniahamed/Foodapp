from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list
    }
    return HttpResponse(template.render(context,request))
    

def item(request):
    return HttpResponse("This is an Item View")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request, 'food/detail.html', context)