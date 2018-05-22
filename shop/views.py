from django.shortcuts import render
from shop.models import productCategory

# Create your views here.

def start(request):
    context = {
        'pCategory': productCategory.objects.all()
    }
    return  render(request, 'index.html', context)


def category(request):
    return  render(request, 'category.html', context={})


def product(request):
    return  render(request, 'product.html', context={})