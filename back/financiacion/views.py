from rest_framework import viewsets

from .models import Financiacion
from .serializers import FinanciacionSerializer

class FinanciacionViewSet(viewsets.ModelViewSet):
    model = Financiacion
    queryset = Financiacion.objects.all()
    serializer_class = FinanciacionSerializer
