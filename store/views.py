from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from company.models import Categories
from .models import Product , ProductCategories

def productPage(request, name):
    category = Categories.objects.get(name=name)
    products = Product.objects.filter(categories=category)
    context = {'category':category, 'products':products}
    template_name = 'product_page.html'

    return render (request, template_name, context)


def productItem(request, slug):
    product = get_object_or_404(ProductCategories, slug=slug)
    context={'product':product}
    template_name = 'product.html'
    return render(request, template_name, context)