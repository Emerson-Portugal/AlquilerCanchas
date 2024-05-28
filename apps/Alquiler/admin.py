from django.contrib import admin
from .models import AccesoriosProducto, Producto, Cliente, Local, Venta, Registro, Administrativa, Caja, DetalleVenta


# Register your models here.


admin.site.register(AccesoriosProducto)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Local)
admin.site.register(Venta)
admin.site.register(Registro)
admin.site.register(Administrativa)
admin.site.register(Caja)
admin.site.register(DetalleVenta)