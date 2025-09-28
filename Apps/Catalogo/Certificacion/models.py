from django.db import models

# Create your models here.
class certificacion(models.Model):
    nombre = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha_emicion = models.DateField()
    fecha_vencimiento = models.DateField()
    archivo = models.FileField(upload_to='Certificaciones/')

    class Meta:
        db_table = 'certificacion'

    def __str__(self):
        return self.nombre