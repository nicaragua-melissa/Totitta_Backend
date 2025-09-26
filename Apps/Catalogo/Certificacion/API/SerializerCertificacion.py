from rest_framework.serializers import ModelSerializer

from Apps.Catalogo.Certificacion.models import certificacion


class CertificacionSerializador(ModelSerializer):
    class Meta:
        model = certificacion
        fields = '__all__'