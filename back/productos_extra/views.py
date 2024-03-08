from rest_framework import viewsets

from .models import Extra
from .serializers import ExtraSerializer

class ExtraViewSet(viewsets.ModelViewSet):
    model = Extra
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
