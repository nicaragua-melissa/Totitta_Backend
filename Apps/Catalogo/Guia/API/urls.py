from rest_framework.routers import DefaultRouter

from Apps.Catalogo.Guia.API.GuiasAPI import GuiasViewSet

routerGuia = DefaultRouter()

routerGuia.register(prefix='guias',basename='guias', viewset=GuiasViewSet)