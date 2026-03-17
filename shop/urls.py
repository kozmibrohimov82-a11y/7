
from django.urls import path

from .views import *

urlpatterns=[
    path('',index,name='home'),
    path('category-by/<slug:category_slug>/',product_by_category,name='category_by_product'),
    path('product/<slug:slug>/', detail_products, name='product_detail'),


]