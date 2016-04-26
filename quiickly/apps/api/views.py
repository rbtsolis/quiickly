# -*- coding: utf-8 -*-

'''
This is an API of quickly team

'''
from rest_framework.decorators import permission_classes
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from apps.products.serializers import ProductSerializer, OrderSerializer
from apps.products.models import Product
from apps.orders.models import Order
from apps.users.models import User, Address
from apps.users.views import base64_to_image
from apps.users.serializers import (
    UserCreateSerializer, UserSerializer, AddressSerializer
)


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

    def list(self, request, *args, **kwargs):

        return super(UserViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            id = int(pk)
        except:
            id = 0

        if request.user.id == id:
            self.serializer_class = UserSerializer
            return super(UserViewSet, self).retrieve(request, *args, **kwargs)
        else:
            raise Http404

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True

        image = base64_to_image(request.POST['avatar'])
        password = request.POST['password']

        hash_password = make_password(
            password=password,
            salt=None,
            hasher='pbkdf2_sha256'
        )

        request.POST['password'] = hash_password

        if image is not None:
            request.POST['avatar'] = image

        return super(UserViewSet, self).create(request, *args, **kwargs)


class AddressViewSet(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CreateUser(APIView):

    '''
     {
        "name": "Nombre Dirección",
        "address": "Calle #12 piso 3",
        "latitude": "40.52456",
        "longitude": "-72.35265",
        "display_name": "Juan Pérez",
        "email": "some@some.com",
        "avatar": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABYlBMVEUAAAAAAABff39ocHBpcHBnbW1mbW1pcXFpcHBnbm5EREBob25pcHBEREBEREBob29nbGtla2tnbW1ncHBob29PT01EREBEREBnb29la2tla2tRcnFqcHBqcHBncHBpb29ka2tEREBiZ2Zla2tlbWxlbm5pb29ncHBob29ka2pmbW1ocHBmcnJpcHBlbGxla2taYV9ma2tpcHBpb29paWhlbGtla2tlb25ocHBnb29EREBiaWhnbGx/f39ob29obm5nb29ka2tla2tocHBpcHBpcHBja2tEREBEREBcYmFncHBpbm5qdHRpcHBrcnJrcXFpb29VVVVpcHBpcHBocHBpcHBla2tjamljaWhpcHBob29nbm5pb29pcHBpb29ob29ncHBmbWxlbWxnbGxpb29ocHBpbm5jbGxVf39pbm5nbGxnbGxpbm5NZGJob29pcHBobm5obm5pcHBnbm5nbW1pcHD6qyPjAAAAbnRSTlMAAQhds87eYURFAZiPAQRp7NfP83UFCQVD/ZQIT3H492kKMPutHafugoK6vBTGvd8iX/5yHN/dNYJAAkn3ApKyeX+1hN/GJA0PLMXwGPUmLXkDS9p605xtVEmQ237VUE7xmYaEgYHtVwZcX19cC0CKXKsAAADSSURBVBgZBcExSwJhAIDh9/WWPPMWh477ASIhgSQEQtTeEDTU4ODgkP2ios2loQgcImiIqKFoMIJoiGhqLFu00uH6eh4BAP0DAAGIdO/AGYAAc7saQrT/C7EApZ6hkHM4oaxgonZz6KsKaftIVdw+cSRxqr5CVTfORxNJKkWfgbrq21gWMtevh9B07cZ7JFlscZrdtXTl6uMdiZdtMlQbhYdLEOrp0pOqtRfPkNWfzM+yYXy7+djwQrZU1eMd1YF0Kl+qwvd8cTqQnhpCBJAb9f8BNuw3lcuFH3IAAAAASUVORK5CYII=",
        "password": "password",
        "phone": "54662548",
        "os": "Android"
    }
    '''

    def get(self, request, pk=None, *args, **kwargs):

        try:
            id = int(pk)
        except:
            id = 0

        if request.user.id == id:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            raise Http404

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):

        image = base64_to_image(request.data['avatar'])
        password = request.data['password']

        hash_password = make_password(
            password=password, salt=None, hasher='pbkdf2_sha256'
        )

        password = hash_password

        if image is not None:
            avatar = image
        else:
            avatar = request.data['avatar']

        user = User(
            display_name=request.data['display_name'],
            email=request.data['email'],
            avatar=avatar,
            password=hash_password,
            phone=request.data['phone'],
            os=request.data['os']
        )

        user.save()

        address = Address(
            name=request.data['name'],
            address=request.data['address'],
            latitude=request.data['latitude'],
            longitude=request.data['longitude']
        )

        address.save()

        user.address.add(address)

        serializer = UserSerializer(user)

        return Response(serializer.data)


create_user = CreateUser.as_view()
