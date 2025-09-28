from rest_framework.routers import DefaultRouter

from Apps.Catalogo.Reserva.API.ReservaAPI import ReservaModelViewSet

routerReserva = DefaultRouter()

routerReserva.register(prefix='Reserva', basename='Reserva', viewset=ReservaModelViewSet)