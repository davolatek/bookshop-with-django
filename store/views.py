from django.shortcuts import render

from .models import Category, Products
# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Products.objects.all()
    return render(request, 'store/home.html', {'products': products})
