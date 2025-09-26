from rest_framework.serializers import ModelSerializer

from Apps.Catalogo.Persona.models import Persona


class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'