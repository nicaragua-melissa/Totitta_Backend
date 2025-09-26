from rest_framework import routers

from Apps.Movimientos.Reseña.API.ReseñaAPI import ReseniaViewSet

routerResenia = routers.DefaultRouter()
routerResenia.register(prefix='resenia',viewset=ReseniaViewSet,basename='resenia')