from django.shortcuts import render

from apps.products.models import Product


def list_products(request):

    products = Product.objects.all()

    products_list = {

        "products" : products

    }

    return render(request, "products.html", products_list)
