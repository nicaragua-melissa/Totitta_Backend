from django.db import models

from Apps.Catalogo.Reserva.models import Reserva


# Create your models here.
class Actividad(models.Model):
    CodigoActividad = models.CharField(max_length=10)
    NombreActividad = models.CharField(max_length=100)
    IdReserva = models.ForeignKey(Reserva,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Actividad'

    def __str__(self):
        return self.CodigoActividad
