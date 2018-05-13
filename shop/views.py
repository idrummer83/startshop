from django.shortcuts import render

# Create your views here.

def start(request):
    return  render(request, 'index.html', context={})


def category(request):
    return  render(request, 'category.html', context={})


def product(request):
    return  render(request, 'product.html', context={})