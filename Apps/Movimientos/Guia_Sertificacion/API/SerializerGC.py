from rest_framework.serializers import ModelSerializer

from Apps.Movimientos.Guia_Sertificacion.models import Guia_Sertificacion


class GCSerializer(ModelSerializer):
    class Meta:
        model = Guia_Sertificacion
        fields = '__all__'