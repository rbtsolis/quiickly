# -*- coding: utf-8 -*-

'''
This is an API of quickly team

'''
from rest_framework.decorators import permission_classes
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
from django.contrib.auth.hashers import make_password


from apps.products.serializers import ProductSerializer, OrderSerializer
from apps.products.models import Product
from apps.orders.models import Order
from apps.users.models import User, Address
from apps.users.views import base64_to_image
from apps.users.serializers import UserCreateSerializer, UserSerializer, AddressSerializer


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


class UserViewSet(viewsets.ModelViewSet):


    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


    def list(self, request):
        raise Http404


    def retrieve(self, request, pk=None, *args, **kwargs):

        try:
            id = int(pk)
        except:
            id = 0

        if request.user.id == int(id):
            self.serializer_class = UserSerializer
            return super(UserViewSet, self).retrieve(request, *args, **kwargs)
        else:
            raise Http404


    def create(self, request, *args, **kwargs):

        request.POST._mutable = True

        image = base64_to_image(request.POST['avatar'])
        password = request.POST['password']

        hash_password = make_password(password=password,
        salt=None,
        hasher='pbkdf2_sha256')

        request.POST['password'] = hash_password

        if image is not None:
            request.POST['avatar'] = image

        return super(UserViewSet, self).create(request, *args, **kwargs)


class AddressViewSet(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@api_view(['PUT'])
def user_address(request):
