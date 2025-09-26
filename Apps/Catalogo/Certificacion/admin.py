from django.contrib import admin

from Apps.Catalogo.Certificacion.models import certificacion


# Register your models here.
@admin.register(certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre','institucion','fecha_emicion','fecha_vencimiento','archivo']