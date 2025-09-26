from rest_framework.routers import DefaultRouter

from Apps.Catalogo.Certificacion.API.CertificacionsAPI import CertificacionModelViewSet

routerCertificacion = DefaultRouter()

routerCertificacion.register(prefix='certificacion', viewset=CertificacionModelViewSet, basename='certificacion')