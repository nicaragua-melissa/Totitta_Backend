from django.contrib import admin

from Apps.Catalogo.Reserva.models import Reserva


# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    search_fields = ['codigoReserva']
    list_display = ['codigoReserva','nombre','latitud','longitud','Correo']