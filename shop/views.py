from django.shortcuts import render
from shop.models import *

# Create your views here.

def start(request):
    context = {
        'pCategory': productCategory.objects.all(),
        'products': Product.objects.all()
    }
    return  render(request, 'index.html', context)


def category(request):
    return  render(request, 'category.html', context={})


def productAll(request):
    products_all = productCategory.objects.all()
    return  render(request, 'product.html', products_all)


def product(request, id):
    prod_inf = {
       'prod': Product.objects.filter(id=id)
    }
    return  render(request, 'product.html', context=prod_inf)