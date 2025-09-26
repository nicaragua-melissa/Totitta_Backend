from rest_framework.routers import DefaultRouter

from Apps.Movimientos.Reservacion.API.ReservacionAPI import ReservacionViewSet

routerReservacion = DefaultRouter()

routerReservacion.register(prefix='Reservacion', basename='Reservacion', viewset=ReservacionViewSet)