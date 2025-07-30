from django.urls import path
from .views import HomePageView, ShopItemView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('item/', ShopItemView.as_view(), name='shop_item'),
]
