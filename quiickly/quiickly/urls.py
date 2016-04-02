"""quiickly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from apps.users.views import login_ajax, Logout

urlpatterns = [
    url(r'^su/', admin.site.urls),
    url(r'^api/v1/', include('apps.api.urls')),
    url(r'^', include('apps.web.urls')),
    url(r'^login/', login_ajax),
    url(r'^logout/', Logout),
    url(r'^api/v1/tokens/create/$', obtain_jwt_token),
    url(r'^api/v1/tokens/refresh/$', refresh_jwt_token),
    url(r'^api/v1/tokens/verify/$', verify_jwt_token),
]

if settings.DEBUG or settings.DEBUG == False:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]
