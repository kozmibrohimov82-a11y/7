from django.shortcuts import render, get_object_or_404

from .models import *

def index(request):
    products=Product.objects.all()
    categories=Category.objects.all()

    context={
        "products":products,
        'categories':categories,
    }
    return render(request,'index.html',context)

def product_by_category(request,category_slug):
    categories=Category.objects.all()
    category=Category.objects.get(slug=category_slug)
    products=Product.objects.filter(category=category)
    context={
        'categories':categories,
        'products':products
    }

    return render(request,'index.html',context)

def detail_products(request,slug):
    product=get_object_or_404(Product,slug=slug)
    context={
        'product':product
    }
    return render(request,'single.html',context)