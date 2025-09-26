from rest_framework.serializers import ModelSerializer

from Apps.Movimientos.Actividad.models import Actividad


class ActividadSerializer(ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'