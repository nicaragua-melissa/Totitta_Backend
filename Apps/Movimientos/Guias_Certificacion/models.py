from django.db import models

from Apps.Catalogo.Certificacion.models import certificacion
from Apps.Movimientos.Guias.models import Guia


# Create your models here.
class Guia_Certificacion(models.Model):
    Id_Certificacion = models.ForeignKey(certificacion, on_delete=models.CASCADE)
    Id_Guia = models.ForeignKey(Guia, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Guia_Certificacion'