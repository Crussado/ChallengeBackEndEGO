from rest_framework import serializers
from .models import Modelo, Parte

class ModeloListSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Modelo
        fields = ('id', 'marca', 'nombre', 'precio', 'anio', 'url_img')

class PartesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    carroceria = serializers.CharField()
    partes = PartesSerializer(many=True)

    class Meta:
        model = Modelo
        fields = '__all__'
