from rest_framework import serializers
from base64 import b64decode
from django.core.files.base import ContentFile
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse

from decimal import Decimal


from apps.users.models import User, Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:

        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'display_name', 'email', 'avatar', 'phone', 'address'
        )
        depth = 1
















class UserCreateSerializer(serializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:

        model = User
        fields = (
            'display_name', 'email', 'password', 'avatar', 'phone', 'os', 'address'
        )
        depth = 1














    '''
    def create(self, validated_data):

        address = dict(validated_data['address'])

        address_created = Address.objects.create(**address)

        del validated_data['address']

        user = User.objects.create(**validated_data)

        user.address.add(address_created)
        print("--------------------------------------------")
        print(user)
        return {'created','true'}
    '''
