from django.contrib import admin

from Apps.Movimientos.Reseña.models import Resenia

# Register your models here.
@admin.register(Resenia)
class ReseñaAdmin(admin.ModelAdmin):
    search_fields = ['fecha_comentario']
    list_display = ['fecha_comentario','comentario','Calificacion','Id_Reserva']