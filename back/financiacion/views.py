from rest_framework import viewsets, mixins

from .models import Financiacion
from .serializers import FinanciacionSerializer

class FinanciacionViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    model = Financiacion
    queryset = Financiacion.objects.all()
    serializer_class = FinanciacionSerializer
