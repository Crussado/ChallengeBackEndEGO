from django.conf.urls import url, include
from rest_framework import routers

from .views import ExtraViewSet

router = routers.SimpleRouter()
router.register(r'extra', ExtraViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
