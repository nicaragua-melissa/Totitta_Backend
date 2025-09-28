from rest_framework.serializers import ModelSerializer

from Apps.Catalogo.Persona.API.SerializerPersona import PersonaSerializer
from Apps.Catalogo.Reserva.API.ReservaSerializer import ReservaSerializer
from Apps.Movimientos.Reservacion.models import Reservacion


class ReservacionSerializer(ModelSerializer):
    Id_Reserva = ReservaSerializer(read_only=True)
    Id_Persona = PersonaSerializer(read_only=True)

    class Meta:
        model = Reservacion
        fields = '__all__'