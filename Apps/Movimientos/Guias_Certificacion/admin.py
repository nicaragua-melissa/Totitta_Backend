from django.contrib import admin

from Apps.Movimientos.Guias_Certificacion.models import Guia_Certificacion


# Register your models here.
@admin.register(Guia_Certificacion)
class Guia_SertificacionAdmin(admin.ModelAdmin):
    list_display = ('Id_Certificacion', 'Id_Guia')