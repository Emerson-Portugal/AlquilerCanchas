from django.db import models

# Create your models here.
from django.db import models

class AccesoriosProducto(models.Model):
    idAccProducto = models.AutoField(primary_key=True)
    nomAccProducto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nomAccProducto

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nomProducto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    idAccProducto = models.ForeignKey(AccesoriosProducto, on_delete=models.CASCADE)
    idLocal = models.ForeignKey('Local', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomProducto

class DetalleVenta(models.Model):
    idDetalleVenta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    munDocumento = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Local(models.Model):
    idLocal = models.AutoField(primary_key=True)
    nomLocal = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nomLocal

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    fechVenta = models.DateField()
    horaVenta = models.TimeField()
    totalVenta = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=255)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idLocal = models.ForeignKey(Local, on_delete=models.CASCADE)
    idCaja = models.ForeignKey('Caja', on_delete=models.CASCADE)

class Registro(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    fechRegistro = models.DateField()
    horaInicio = models.TimeField()
    duracion = models.IntegerField()
    estado = models.CharField(max_length=255)
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.CharField(max_length=255)
    idAdministrativa = models.ForeignKey('Administrativa', on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idLocal = models.ForeignKey(Local, on_delete=models.CASCADE)
    idCaja = models.ForeignKey('Caja', on_delete=models.CASCADE)

class Administrativa(models.Model):
    idAdministrativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    munDocumento = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    idLocal = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Caja(models.Model):
    idCaja = models.AutoField(primary_key=True)
    horaApertura = models.TimeField()
    fechaApertura = models.DateField()
    montoApertura = models.DecimalField(max_digits=10, decimal_places=2)
    horaCierra = models.TimeField(null=True, blank=True)
    fechaCierre = models.DateField(null=True, blank=True)
    montoCierre = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    idLocal = models.ForeignKey(Local, on_delete=models.CASCADE)
    idAdministrativa = models.ForeignKey(Administrativa, on_delete=models.CASCADE)
