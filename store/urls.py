from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('books/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_list>', views.category_list, name='category_list')
]