from django.shortcuts import render, get_object_or_404
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


def productAll(request, category_slug=None):
    category = None
    categories = productCategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(productCategory, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return  render(request, 'product.html', context)


def product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return  render(request, 'product.html', context)