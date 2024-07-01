from django.db import models

class Local(models.Model):
    idLocal = models.AutoField(primary_key=True)
    nomLocal = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nomLocal

class Cancha(models.Model):
    idCancha = models.AutoField(primary_key=True)
    nomCancha = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    idLocal = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomCancha

class Horario(models.Model):
    idHorario = models.AutoField(primary_key=True)
    horaInicio = models.DecimalField(max_digits=5, decimal_places=2)
    horaFin = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.horaInicio} - {self.horaFin}"

class AccesoriosProducto(models.Model):
    idAccProducto = models.AutoField(primary_key=True)
    nomAccProducto = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nomAccProducto

class ReservaCancha(models.Model):
    idReservaCancha = models.AutoField(primary_key=True)
    fechRegistro = models.DateField(auto_now_add=True)
    duracion = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.BooleanField(default=True)
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    idAccProducto = models.ForeignKey(AccesoriosProducto, on_delete=models.SET_NULL, null=True)
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.idReservaCancha}"

class DetalleReserva(models.Model):
    idDetalleReserva = models.AutoField(primary_key=True)
    idReservaCancha = models.ForeignKey(ReservaCancha, on_delete=models.CASCADE)
    idCancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
