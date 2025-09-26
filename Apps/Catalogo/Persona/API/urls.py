from rest_framework.routers import DefaultRouter

from Apps.Catalogo.Persona.API.PersonaAPI import PersonaViewSet

routerPersona = DefaultRouter()

routerPersona.register(prefix='persona', basename="persona", viewset=PersonaViewSet)