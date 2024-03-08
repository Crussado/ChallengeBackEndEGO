from rest_framework import serializers
from .models import Financiacion

class FinanciacionSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField() # TODO
    
    class Meta:
        model = Financiacion
        fields = '__all__'
