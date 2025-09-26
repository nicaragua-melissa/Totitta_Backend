from rest_framework.routers import DefaultRouter

from Apps.Movimientos.Actividad.API.ActividadAPI import ActividadViewSet

routerActividad = DefaultRouter()

routerActividad.register(prefix='actividad', viewset=ActividadViewSet, basename='actividad')