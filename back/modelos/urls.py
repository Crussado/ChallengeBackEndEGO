from django.conf.urls import url, include
from rest_framework import routers

from .views import ModeloViewSet

router = routers.SimpleRouter()
router.register(r'modelo', ModeloViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
