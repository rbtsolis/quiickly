# -*- coding: utf-8 -*-

'''
This is an API of quickly team

'''
from rest_framework.decorators import permission_classes
from rest_framework import permissions, viewsets
from apps.products.serializers import ProductSerializer
from apps.products.models import Product


'''

This is a function to get all details of the product

'''
#@permission_classes((permissions.IsAuthenticated, ))
class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

