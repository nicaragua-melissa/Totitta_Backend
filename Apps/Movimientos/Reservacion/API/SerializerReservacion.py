from rest_framework.serializers import ModelSerializer

from Apps.Movimientos.Reservacion.models import Reservacion


class ReservacionSerializer(ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'