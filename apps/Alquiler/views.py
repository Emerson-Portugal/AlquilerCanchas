# views.py
from rest_framework import viewsets
from .models import Local, Cancha, Horario, AccesoriosProducto, ReservaCancha, DetalleReserva
from .serializers import LocalSerializer, CanchaSerializer, HorarioSerializer, AccesoriosProductoSerializer, ReservaCanchaSerializer, DetalleReservaSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class AccesoriosProductoViewSet(viewsets.ModelViewSet):
    queryset = AccesoriosProducto.objects.all()
    serializer_class = AccesoriosProductoSerializer

class ReservaCanchaViewSet(viewsets.ModelViewSet):
    queryset = ReservaCancha.objects.all()
    serializer_class = ReservaCanchaSerializer

class DetalleReservaViewSet(viewsets.ModelViewSet):
    queryset = DetalleReserva.objects.all()
    serializer_class = DetalleReservaSerializer
