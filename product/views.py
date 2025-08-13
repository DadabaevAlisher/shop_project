from django.shortcuts import render
from .models import *
# Create your views here.

def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products_list.html", context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, "product_detail.html", context)