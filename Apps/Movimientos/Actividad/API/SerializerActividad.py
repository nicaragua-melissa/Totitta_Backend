from rest_framework.serializers import ModelSerializer

from Apps.Movimientos.Actividad.models import Actividad
from Apps.Movimientos.Reservacion.API.SerializerReservacion import ReservacionSerializer


class ActividadSerializer(ModelSerializer):
    IdReserva = ReservacionSerializer(read_only=True)

    class Meta:
        model = Actividad
        fields = '__all__'