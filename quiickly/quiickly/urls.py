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
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from apps.store import urls as store_urls

from apps.users.views import login_ajax, Logout, CreateUser

urlpatterns = [
    url(r'^su/', admin.site.urls),
    url(r'^api/', include('apps.api.urls')),
    url(r'^', include('apps.web.urls')),
    url(r'^tienda/', include(store_urls)),
    url(r'^droguerias/', include('apps.drugstores.urls')),
    url(r'^login/', login_ajax),
    url(r'^logout/', Logout),
]

if settings.DEBUG or settings.DEBUG == False:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
