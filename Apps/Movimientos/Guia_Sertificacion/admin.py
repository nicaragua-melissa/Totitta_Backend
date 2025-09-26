from django.contrib import admin

from Apps.Movimientos.Guia_Sertificacion.models import Guia_Sertificacion


# Register your models here.
@admin.register(Guia_Sertificacion)
class Guia_SertificacionAdmin(admin.ModelAdmin):
    list_display = ('Id_Certificacion', 'Id_Guia')