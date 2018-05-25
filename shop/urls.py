
from django.conf.urls import url, include
# from account import views as accounts_views
from shop.views import *



urlpatterns = [
    # url(r'^/$', start, name='products_all'),
    url(r'^(?P<id>\d+)/$', product, name='product'),
]