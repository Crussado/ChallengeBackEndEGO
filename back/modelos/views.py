from django.http import JsonResponse
from django.db.models import Q

from rest_framework.decorators import action
from rest_framework import viewsets, mixins, status

from .models import Modelo, Parte
from .serializers import ModeloSerializer, ModeloListSerializer

class ModeloViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    model = Modelo
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

    serializers = {
        'retrieve': ModeloSerializer,
        'list': ModeloListSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)

    @action(detail=False, methods=['get'])
    def toyota_gazoo_racing(self, request):
        '''
           Api para la seccion de navegacion Toyota Gazoo Racing, suponiendo que es un modelo
           lo devuelve. 
        '''
        try:
            modelo = Modelo.objects.get(marca='Toyota', modelo='Gazoo Racing')
            data = self.serializer_class(modelo).data
            response = JsonResponse(data, status=status.HTTP_200_OK)
        except Modelo.DoesNotExist:
            response = JsonResponse({'error': 'Modelo inexistente.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

    @action(detail=False, methods=['get'])
    def toyota_hibridos(self, request):
        '''
           Api para la seccion de navegacion Toyota hibridos, devuelve los modelos de Toyota
           con transmision automatica y manual.
        '''
        try:
            partes = Parte.objects.filter(Q(nombre='Transmision automatica') | Q(nombre='Transmision manual'))
            if partes.count() != 2:
                raise Exception

            modelos = Modelo.objects.filter(partes=partes.first()).filter(partes=partes.last())
            data = self.serializer_class(modelos, many=True).data

            response = JsonResponse(data, status=status.HTTP_200_OK)
        except Exception as ex:
            response = JsonResponse({'error': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

    
    @action(detail=False, methods=['get'])
    def innovacion(self, request):
        '''
           Api para la seccion de navegacion Innovacion, devuelve los ultimos 5 modelos sacados
           al mercado.
        '''
        try:
            modelos = Modelo.objects.order_by('-anio')[:5]

            data = self.serializer_class(modelos, many=True).data
            response = JsonResponse(data, status=status.HTTP_200_OK)
        except Exception as ex:
            response = JsonResponse({'error': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response
