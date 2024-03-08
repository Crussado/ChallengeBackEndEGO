from django.conf.urls import url, include
from rest_framework import routers

from .views import FinanciacionViewSet

router = routers.SimpleRouter()
router.register(r'financiacion', FinanciacionViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
