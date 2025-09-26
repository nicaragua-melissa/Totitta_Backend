from django.db import models

from Apps.Catalogo.Persona.models import Persona
from Apps.Catalogo.Reserva.models import Reserva


# Create your models here.
class Reservacion(models.Model):
    Codigo_Reserva = models.CharField(max_length=10)
    Fecha_Actual = models.DateField()
    Fecha_Reserva = models.DateField()
    Precio = models.DecimalField(decimal_places=2, max_digits=10)
    Id_Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Id_Reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Reservacion'

    def __str__(self):
        return self.Codigo_Reserva