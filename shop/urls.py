
from django.conf.urls import url, include
# from account import views as accounts_views
from . import views

app_name = 'shop'

urlpatterns = [
    # url(r'^/$', start, name='products_all'),
    # url(r'^(?P<id>\d+)/$', product, name='product'),


url(r'^$', views.productAll, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.productAll, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product, name='product_detail'),
]