from Config.urls import path, include


urlpatterns = [
    path('Usuario/', include('Seguridad.usuarios.urls')),
]