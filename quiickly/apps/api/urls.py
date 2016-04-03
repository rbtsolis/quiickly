from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductViewSet, OrderViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
