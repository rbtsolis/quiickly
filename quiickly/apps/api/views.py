# -*- coding: utf-8 -*-

'''
This is an API of quickly team

'''
from rest_framework.decorators import permission_classes
from rest_framework import permissions, viewsets
from apps.products.serializers import ProductSerializer, OrderSerializer
from apps.products.models import Product, Order


'''

This is a function to get all details of the product

'''
class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super(ProductViewSet, self).list(request, *args, **kwargs)


@permission_classes((permissions.IsAuthenticated, ))
class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
