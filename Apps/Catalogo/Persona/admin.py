from django.contrib import admin

from Apps.Catalogo.Persona.models import Persona


# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['Identificacion']
    list_display = ['Identificacion', 'Turista', 'Nombre','Nombre2','Apellido1','Apellido2','Edad','Sexo']