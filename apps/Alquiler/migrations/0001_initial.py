# Generated by Django 5.0.6 on 2024-05-28 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccesoriosProducto',
            fields=[
                ('idAccProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nomAccProducto', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Administrativa',
            fields=[
                ('idAdministrativa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('munDocumento', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('munDocumento', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('idLocal', models.AutoField(primary_key=True, serialize=False)),
                ('nomLocal', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('idCaja', models.AutoField(primary_key=True, serialize=False)),
                ('horaApertura', models.TimeField()),
                ('fechaApertura', models.DateField()),
                ('montoApertura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('horaCierra', models.TimeField(blank=True, null=True)),
                ('fechaCierre', models.DateField(blank=True, null=True)),
                ('montoCierre', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('idAdministrativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.administrativa')),
                ('idLocal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.local')),
            ],
        ),
        migrations.AddField(
            model_name='administrativa',
            name='idLocal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.local'),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nomProducto', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=255)),
                ('idAccProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.accesoriosproducto')),
                ('idLocal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.local')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idRegistro', models.AutoField(primary_key=True, serialize=False)),
                ('fechRegistro', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('duracion', models.IntegerField()),
                ('estado', models.CharField(max_length=255)),
                ('pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comentario', models.CharField(max_length=255)),
                ('idAdministrativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.administrativa')),
                ('idCaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.caja')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.cliente')),
                ('idLocal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.local')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False)),
                ('fechVenta', models.DateField()),
                ('horaVenta', models.TimeField()),
                ('totalVenta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=255)),
                ('idCaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.caja')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.cliente')),
                ('idLocal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.local')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('idDetalleVenta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precioVenta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.producto')),
                ('idVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.venta')),
            ],
        ),
    ]
