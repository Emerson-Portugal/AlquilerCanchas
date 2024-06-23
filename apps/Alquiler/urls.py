# alquiler/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocalViewSet, CanchaViewSet, HorarioViewSet, AccesoriosProductoViewSet, ReservaCanchaViewSet, DetalleReservaViewSet


app_name = 'alquiler'  # Define el espacio de nombres aquí

router = DefaultRouter()
router.register(r'locales', LocalViewSet)
router.register(r'canchas', CanchaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'accesorios', AccesoriosProductoViewSet)
router.register(r'reservas', ReservaCanchaViewSet)
router.register(r'detalles', DetalleReservaViewSet)


urlpatterns = [
    path('listado/', include(router.urls)),
]