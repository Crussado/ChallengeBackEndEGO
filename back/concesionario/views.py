from rest_framework import viewsets, mixins

from .models import Concesionario
from .serializers import ConcesionarioSerializer

class ConcesionarioViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    model = Concesionario
    queryset = Concesionario.objects.all()
    serializer_class = ConcesionarioSerializer

