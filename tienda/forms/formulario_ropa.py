from django import forms
from tienda.models.ropa import Ropa

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = ['nombre', 'color', 'talla']
