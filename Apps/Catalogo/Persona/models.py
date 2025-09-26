from django.db import models

#Se creara la opcion de ser local o internacional
#Con el fin de evitar la informacion redundante
Tipo_Persona = [
    ('NAC', 'Nacional'),
    ('INT', 'Internacional'),
]

Genero = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('ND', 'Prefiero no decirlo'),
]

# Create your models here.
class Persona(models.Model):
    Identificacion=models.CharField(verbose_name='Identificacion',max_length=20)
    Turista=models.CharField(verbose_name='Turista',max_length=14, choices=Tipo_Persona, default='Nacional')
    Nombre=models.CharField(verbose_name='Primer_Nombre',max_length=50)
    Nombre2=models.CharField(verbose_name='Segundo_Nombre',max_length=50)
    Apellido1=models.CharField(verbose_name='Primer_Apellido',max_length=50)
    Apellido2=models.CharField(verbose_name='Segundo_Apellido',max_length=50)
    Edad=models.IntegerField(verbose_name='Edad')
    Sexo=models.CharField(verbose_name='Sexo',max_length=20, choices=Genero, default='Masculino')
    is_Active = models.BooleanField(verbose_name='Activo', default=True)

    class Meta:
        db_table = 'persona'

    def __str__(self):
        return self.Identificacion