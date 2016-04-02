from jwt import encode, decode
from django.conf import settings
from apps.users.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user).data
    }


def create_token(payload):

    token   = encode(payload, settings.SECRET_KEY, algorithm='HS512')



def decode_token(token):

    try:
        payload_decode = decode(token, settings.SECRET_KEY, algorithms=['HS512'])
    except:
        payload_decode = "This token has expired"

    return payload_decode
