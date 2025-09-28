from rest_framework.serializers import ModelSerializer

from Apps.Movimientos.Guias.models import Guia
from Apps.Movimientos.Reservacion.API.SerializerReservacion import ReservacionSerializer


class GuiasSerializer(ModelSerializer):
    IdReserva = ReservacionSerializer(read_only=True)

    class Meta:
        model = Guia
        fields = '__all__'