from django.contrib import admin

from Apps.Movimientos.Reservacion.models import Reservacion


# Register your models here.
@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Reserva']
    list_display = ('Codigo_Reserva','Fecha_Actual','Fecha_Reserva','Precio','Id_Persona','Id_Reserva')
