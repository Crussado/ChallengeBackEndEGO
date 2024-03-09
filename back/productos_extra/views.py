from django.http import JsonResponse

from rest_framework import viewsets, mixins, status
from rest_framework.decorators import list_route

from .models import Extra
from .serializers import ExtraSerializer

class ExtraViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    model = Extra
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer

    @list_route(methods=['get'])
    def toyota_mobility_service(self, request):
        '''
           Api para la seccion de navegacion Toyota Mobility Service, devuelve los servicios de movilidad
           de relacionado con Toyota.
        '''
        try:
            servicio_nombre = 'Toyota Mobility'
            servicios = Extra.objects.filter(tipo=True, nombre__icontains=servicio_nombre)
            
            data = self.serializer_class(servicios, many=True).data
            response = JsonResponse(data=data, status=status.HTTP_200_OK)
        except Exception as ex:
            response = JsonResponse({'error': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response
