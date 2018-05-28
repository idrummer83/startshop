from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shop.models import *

# Create your views here.

@login_required
def soc(request):
    context = {
        'pCategory': productCategory.objects.all(),
        'products': Product.objects.all()
    }
    return  render(request, 'social.html', context)