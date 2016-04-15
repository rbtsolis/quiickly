from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.hashers import make_password
from decimal import Decimal

from base64 import b64decode
from django.core.files.base import ContentFile

from .models import Address, User
from .forms import AddressForm


def make_random_password(length):
    allowed_chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    from random import SystemRandom as random
    return ''.join([random().choice(allowed_chars) for i in range(length)])


def Logout(request):
    logout(request)
    return redirect('/')


'''
    This is Login with AJAX, require: email and password
    first this function need authenticate and later login
'''
def login_ajax(request):

    if request.is_ajax():

        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username = username,
            password = password)
        if user is not None and user.is_active:
            login(request, user)
            response = JsonResponse({'status_login': 'success'})
        else:
            response = JsonResponse({'status_login': 'error'})
        return HttpResponse(response.content)
    else:
        raise Http404


'''
This function is only execute when the user choose a custom picture
'''
def CreateUser(request):

    if request.is_ajax():

        '''
        password = request.POST['password']
        display_name = request.POST['display_name']
        email = request.POST['email']
        avatar = request.POST['avatar']
        avatar = base64_to_image(avatar)
        phone= request.POST['phone']
        os= request.POST['os']
        name = 'some name'
        '''

        address_name= request.POST['address_name']
        address = request.POST['address']
        latitude = Decimal(request.POST['latitude'])
        longitude = Decimal(request.POST['longitude'])

        print("%s %s"%(latitude,longitude))


        address_form = AddressForm(
            name='name', address='asdasdasd',
            latitude=latitude, longitude=longitude
        )

        print(address_form)

        if address_form.is_valid():
            print("Address is valid")
            address_user = Address.objects.create(
                name=address_name,address=address,
                latitude=latitud, longitude=longitud
            )
        else:
            print("Formulario inválido")


        '''
        hash_password = make_password(password=password,
        salt=None,
        hasher='pbkdf2_sha256')
        '''

        #try:
        '''
        address_user = Address.objects.create(
            name=address_name,address=address,latitude=latitud, longitude=longitud
        )
        '''

        '''
        except:
            response = JsonResponse({ 'status_address' : 'error' })
            return HttpResponse(response.content)
        '''

        '''
        address_2 = Address.objects.get(id=4)

        #try:
        user = User.objects.create(
            name=name, display_name=display_name, password=password,email=email,
            avatar=avatar, phone=phone, os=os
        )



        user.address.add(address_2)
        '''
        '''
        except:
            response = JsonResponse({ 'status_user' : 'error' })
            return HttpResponse(response.content)
        '''

        response = JsonResponse({ 'request' : 'True' })
        return HttpResponse(response.content)

    else:
        raise Http404


def base64_to_image(data):

        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(b64decode(imgstr), name="%s.%s"%(make_random_password(10), ext))

            return data
