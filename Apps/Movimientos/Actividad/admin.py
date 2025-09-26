from django.contrib import admin

from Apps.Movimientos.Actividad.models import Actividad


# Register your models here.
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    search_fields = ['CodigoActividad']
    list_display = ['CodigoActividad','NombreActividad','IdReserva']