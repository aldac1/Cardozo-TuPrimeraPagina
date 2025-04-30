from django import forms
from tienda.models.ropa import Ropa


class RopaForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Ropa
        fields = ["nombre", "color", "talla", "imagen"]

