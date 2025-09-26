from rest_framework.serializers import ModelSerializer

from Apps.Catalogo.Guia.models import Guia


class GuiasSerializer(ModelSerializer):
    class Meta:
        model = Guia
        fields = '__all__'