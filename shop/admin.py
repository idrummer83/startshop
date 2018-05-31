from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
# from sorl.thumbnail.admin import AdminImageMixin

from .models import *
# Register your models here.



@admin.register(productCategory)
class productCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at', 'published')
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at')
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
