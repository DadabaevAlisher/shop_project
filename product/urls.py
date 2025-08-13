from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.products_list, name='product_list'),
    path('product_detail/', views.product_detail, name='product_detail')
]
