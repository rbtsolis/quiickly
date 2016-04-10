from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductViewSet, OrderViewSet
from .tokens import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    url(r'^v1/tokens/create/$', obtain_auth_token),
    url(r'^v1/', include(router.urls)),
]
