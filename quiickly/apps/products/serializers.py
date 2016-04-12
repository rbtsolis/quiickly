# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.orders.models import Order
from .models import Product


'''

This is a class to serialize the products objects

'''
class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = (
            'id', 'name', 'brand', 'type',
            'stock', 'state', 'price', 'image'
        )


'''
This is a class to serialize the Orders objects

'''
class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = '__all__'
