from django.db import models

from Apps.Catalogo.Reserva.models import Reserva


# Create your models here.
class Resenia(models.Model):
    comentario = models.TextField()
    Calificacion = models.IntegerField()
    fecha_comentario = models.DateField()
    Id_Reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Resenia'

    def __str__(self):
        return str(self.fecha_comentario)