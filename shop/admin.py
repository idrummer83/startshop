from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from .models import *

# Register your models here.

# @admin.register(Product)
class ProductAdmin(models.Model):
    model = productCategory
    list_display = ('id', 'name', 'slug', 'published', 'image', 'description', 'long_description')