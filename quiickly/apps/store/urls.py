from django.conf.urls import url

from .views import list_products

urlpatterns = [
    url(r'^$', list_products),
]
