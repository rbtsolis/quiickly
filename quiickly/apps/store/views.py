from django.shortcuts import render

from apps.products.models import Product


def list_products(request):
    return render(request, "products.html")
