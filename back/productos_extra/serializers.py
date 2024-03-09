from rest_framework import serializers
from .models import Extra

class ExtraSerializer(serializers.ModelSerializer):
    tipo = serializers.SerializerMethodField()

    class Meta:
        model = Extra
        fields = '__all__'

    def get_tipo(self, obj):
        return dict(Extra.tipos)[obj.tipo]
