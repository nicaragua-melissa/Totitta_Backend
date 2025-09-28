from django.contrib import admin

from Apps.Movimientos.Guias.models import Guia


# Register your models here.
@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    search_fields = ['cedula']
    list_display = ['cedula','Nombre1','Nombre2','Apellido1','Apellido2','Edad','Sexo','Telefono','Dirrecion','is_Active','id_Reserva']