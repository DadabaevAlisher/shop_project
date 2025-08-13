from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.products_list),
    path("detail/<int:product_id>", views.product_detail)
]
