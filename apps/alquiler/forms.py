from django import forms
from .models import ReservaCancha, DetalleReserva, Cancha, Horario

class ReservaCanchaForm(forms.ModelForm):
    class Meta:
        model = ReservaCancha
        fields = ['duracion', 'pago', 'idAccProducto', 'idHorario']
        widgets = {
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'pago': forms.NumberInput(attrs={'class': 'form-control'}),
            'idAccProducto': forms.Select(attrs={'class': 'form-control'}),
            'idHorario': forms.Select(attrs={'class': 'form-control'}),
        }

class DetalleReservaForm(forms.ModelForm):
    class Meta:
        model = DetalleReserva
        fields = ['idCancha']
        widgets = {
            'idCancha': forms.Select(attrs={'class': 'form-control'}),
        }
