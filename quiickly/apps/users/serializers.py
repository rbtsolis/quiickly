from rest_framework import serializers
from base64 import b64decode
from django.core.files.base import ContentFile
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse

from decimal import Decimal


from apps.users.models import User, Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id','display_name', 'email', 'avatar', 'phone', 'address'
        )
        depth = 1


class AddressSerializer(serializers.ModelSerializer):

    class Meta:

        model = Address
        fields = (
            'id', 'name', 'address', 'latitude', 'longitude'
        )


class UserCreateSerializer(serializers.ModelSerializer):


    class Meta:

        model = User
        fields = (
            'display_name', 'password', 'email', 'avatar', 'phone', 'os'
        )
