from rest_framework.routers import DefaultRouter

from Apps.Movimientos.Guias_Certificacion.API.GCAPI import GCViewSet

routerGC = DefaultRouter()

routerGC.register(prefix='Guias_Certificacion', basename='Guias_Certificacion', viewset=GCViewSet)