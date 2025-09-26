from django.db import models

# Create your models here.
class Reserva(models.Model):
    codigoReserva = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    Correo = models.CharField(max_length=100)

    class Meta:
        db_table = 'Reserva'

    def __str__(self):
        return self.codigoReserva