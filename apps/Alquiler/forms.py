from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nomProducto', 'precio', 'descripcion', 'imagen', 'idAccProducto', 'idLocal']
