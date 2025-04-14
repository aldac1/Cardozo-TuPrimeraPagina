from django import forms
from tienda.models.cliente import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', "apellido", 'email', 'telefono', 'direccion']
