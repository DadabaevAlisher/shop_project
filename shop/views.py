from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class ShopItemView(TemplateView):
    template_name = 'shop_item.html'



