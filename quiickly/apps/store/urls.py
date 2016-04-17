from django.conf.urls import url

from .views import principal_store_view

urlpatterns = [
    url(r'^$', principal_store_view),
]
