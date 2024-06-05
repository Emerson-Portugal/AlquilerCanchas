from django import forms
from .models import Cancha

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['nomCancha', 'precio', 'descripcion', 'imagen', 'idLocal']
