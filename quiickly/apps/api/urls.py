from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
