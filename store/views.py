from django.shortcuts import get_object_or_404, render

from .models import Category, Products
# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Products.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):

    product = get_object_or_404(Products, slug=slug, in_stock=True)
    return render(request, 'store/product/detail.html', {'product':product})

def category_list(request, category_list):
    category = get_object_or_404(Category, slug=category_list)
    product = Products.objects.filter(category=category)
    return render(request,'store/product/category.html',{'category': category,'product':product})

