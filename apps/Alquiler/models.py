from django.db import models

class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    numDocumento = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True  # Marcar Persona como clase abstracta


class Cliente(Persona):
    # No necesitas definir idCliente aquí, Django lo manejará automáticamente
    class Meta:
        verbose_name_plural = "Clientes"


class Local(models.Model):
    idLocal = models.AutoField(primary_key=True)
    nomLocal = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nomLocal

class Cancha(models.Model):
    idCancha = models.AutoField(primary_key=True)
    nomCancha = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='canchas/')
    idLocal = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomCancha

class Horario(models.Model):
    idHorario = models.AutoField(primary_key=True)
    horaInicio = models.DecimalField(max_digits=5, decimal_places=2)
    horaFin = models.DecimalField(max_digits=5, decimal_places=2)

class AccesoriosProducto(models.Model):
    idAccProducto = models.AutoField(primary_key=True)
    nomAccProducto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nomAccProducto

class ReservaCancha(models.Model):
    idReservaCancha = models.AutoField(primary_key=True)
    fechRegistro = models.DateField()
    duracion = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField()
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    idAccProducto = models.ForeignKey(AccesoriosProducto, on_delete=models.CASCADE)
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    idCancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)

class DetalleReserva(models.Model):
    idDetalleReserva = models.AutoField(primary_key=True)
    idReservaCancha = models.ForeignKey(ReservaCancha, on_delete=models.CASCADE)
    idCancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    fechVenta = models.DateField()
    horaVenta = models.TimeField()
    totalVenta = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField()
    idReservaCancha = models.ForeignKey(ReservaCancha, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cambiado a Cliente en lugar de Persona

    def __str__(self):
        return f"Venta {self.idVenta} - Cliente: {self.idCliente.nombre}"

class DetalleVenta(models.Model):
    idDetalleVenta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)

