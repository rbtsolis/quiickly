from django.conf.urls import url, include

from .views import landing_view


urlpatterns = [
    url(r'^$', landing_view),
]
