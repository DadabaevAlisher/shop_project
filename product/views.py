from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def products_list(request):
    return render(request, 'products_list.html')

def product_detail(request):
    return render(request, 'product_detail.html')
