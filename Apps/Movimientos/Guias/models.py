from django.db import models

from Apps.Catalogo.Reserva.models import Reserva

# Create your models here.

Genero = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('ND', 'Prefiero no decirlo'),
]


class Guia(models.Model):
    cedula = models.CharField(max_length=18)
    Nombre1 = models.CharField(max_length=50)
    Nombre2 = models.CharField(max_length=50)
    Apellido1 = models.CharField(max_length=50)
    Apellido2 = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Sexo = models.CharField(verbose_name='Sexo', max_length=20, choices=Genero, default='Masculino')
    Telefono = models.CharField(verbose_name='Telefono', max_length=20)
    Dirrecion = models.CharField(verbose_name='Direccion', max_length=200)
    is_Active = models.BooleanField(verbose_name='Activo', default=True)
    id_Reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Guia'

    def __str__(self):
        return self.cedula