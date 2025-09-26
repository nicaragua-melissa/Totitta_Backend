from rest_framework.serializers import ModelSerializer

from Apps.Catalogo.Reserva.models import Reserva


class ReservaSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
