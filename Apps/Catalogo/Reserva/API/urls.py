from rest_framework.routers import DefaultRouter

from Apps.Catalogo.Persona.API.PersonaAPI import PersonaViewSet

routerReserva = DefaultRouter()

routerReserva.register(prefix='Reserva', basename='Reserva', viewset=PersonaViewSet)