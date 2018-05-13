from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
# from sorl.thumbnail.admin import AdminImageMixin

from .models import *

# Register your models here.

@admin.register(baseImage)
class baseImageAdmin(admin.ModelAdmin):
    pass


@admin.register(productCategory)
class productCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'published')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'published', 'description')
