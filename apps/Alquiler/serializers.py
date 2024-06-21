# serializers.py
from rest_framework import serializers
from .models import Local, Cancha, Horario, AccesoriosProducto, ReservaCancha, DetalleReserva

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class AccesoriosProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccesoriosProducto
        fields = '__all__'

class ReservaCanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaCancha
        fields = '__all__'

class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReserva
        fields = '__all__'
