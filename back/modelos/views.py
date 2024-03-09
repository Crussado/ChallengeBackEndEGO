from rest_framework import viewsets

from .models import Modelo
from .serializers import ModeloSerializer, ModeloListSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    model = Modelo
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

    serializers = {
        'retrieve': ModeloSerializer,
        'list': ModeloListSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)
