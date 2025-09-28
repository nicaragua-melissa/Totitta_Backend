from rest_framework.serializers import ModelSerializer

from Apps.Movimientos.Guias_Certificacion.models import Guia_Certificacion


class GCSerializer(ModelSerializer):
    class Meta:
        model = Guia_Certificacion
        fields = '__all__'