from django.conf.urls import url, include
from rest_framework import routers

from .views import ConcesionarioViewSet

router = routers.SimpleRouter()
router.register(r'concesionario', ConcesionarioViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
