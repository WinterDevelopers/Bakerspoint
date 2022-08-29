from re import template
from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = 'index.html'

    return render(request,template_name)

def orderPage(request):
    template_name = 'order.html'

    return render(request,template_name)