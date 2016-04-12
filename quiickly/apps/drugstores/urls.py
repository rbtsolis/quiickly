from django.conf.urls import url

from .views import panel_index

urlpatterns = [
    url(r'^$', panel_index),
]
