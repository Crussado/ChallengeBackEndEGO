# from django.shortcuts import render
from rest_framework import viewsets

from .models import Concesionario
from .serializers import ConcesionarioSerializer

class ConcesionarioViewSet(viewsets.ModelViewSet):
    model = Concesionario
    queryset = Concesionario.objects.all()
    serializer_class = ConcesionarioSerializer

