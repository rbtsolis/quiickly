from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exemp


def make_random_password(length=20,
    allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
    from random import SystemRandom as random
    return ''.join([random().choice(allowed_chars) for i in range(length)])


def Logout(request):
    logout(request)
    return redirect('/')


'''
    This is Login with AJAX, require: email and password
    first this function need authenticate and later login

'''
@csrf_exempt
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

        UserForm = UserForm(request.POST, request.FILES)

        password = request.POST['password']
        hash_password = make_password(password=password,
        salt=None,
        hasher='pbkdf2_sha256')

        if PicForm.is_valid():
            instance = ProfilePicture(avatar=request.FILES['avatar'])
            instance.save()
            image_name = instance.avatar.url
            url_avatar = DOMAIN_URL + image_name  # DOMAIN_URL is definied up

            try:
                new_user = User()
                new_user.username     = request.POST['username']
                new_user.email        = request.POST['email']
                new_user.first_name   = request.POST['first_name']
                new_user.last_name    = request.POST['last_name']
                new_user.gender       = request.POST['gender']
                new_user.password     = hash_password
                new_user.avatar       = url_avatar
                new_user.verify_code  = make_random_password()
                new_user.save()
                response = JsonResponse({'register_status': 'success'})
            except:
                response = JsonResponse({'register_status': 'error catch'})
        else:
            response = JsonResponse({'register_status': 'error validate image'})
        return HttpResponse(response.content)
    else:
        raise Http404
