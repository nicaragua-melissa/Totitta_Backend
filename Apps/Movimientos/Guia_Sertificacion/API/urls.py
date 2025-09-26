from rest_framework.routers import DefaultRouter

from Apps.Movimientos.Guia_Sertificacion.API.GCAPI import GCViewSet

routerGC = DefaultRouter()

routerGC.register(prefix='Guias_Sertificacion', basename='Guia_Sertificacion', viewset=GCViewSet)