from rest_framework import viewsets, mixins

from .models import Extra
from .serializers import ExtraSerializer

class ExtraViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    model = Extra
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
