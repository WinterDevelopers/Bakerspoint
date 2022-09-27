from django.shortcuts import render
from .models import Categories
# Create your views here.

def index(request):
    cake = Categories.objects.get(name='cakes')
    cookies = Categories.objects.get(name='cookies')
    chin_chin = Categories.objects.get(name='chin-chin')
    peanut = Categories.objects.get(name='peanut')

    context = {'cake':cake, 'cookies':cookies,'chinchin':chin_chin,
                'peanut':peanut}
    template_name = 'index.html'

    return render(request,template_name, context)

def orderPage(request):
    template_name = 'order.html'

    return render(request,template_name)