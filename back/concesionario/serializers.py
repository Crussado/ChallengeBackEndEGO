from rest_framework import serializers
from .models import Concesionario

class ConcesionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concesionario
        fields = '__all__'

