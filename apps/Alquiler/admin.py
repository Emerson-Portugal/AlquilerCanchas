from django.contrib import admin
from .models import Cliente, Local, Cancha, Horario, AccesoriosProducto, ReservaCancha, DetalleReserva, Venta, DetalleVenta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Local)
admin.site.register(Cancha)
admin.site.register(Horario)
admin.site.register(AccesoriosProducto)
admin.site.register(ReservaCancha)
admin.site.register(DetalleReserva)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
