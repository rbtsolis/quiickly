from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id','name', 'email', 'avatar', 'phone', 'address'
        )
        depth = 1
