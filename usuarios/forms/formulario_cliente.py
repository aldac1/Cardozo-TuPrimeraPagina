from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.SelectDateWidget(years=range(1900, 2024))
    )
    dni = forms.CharField(label="DNI")
    sexo = forms.ChoiceField(
        label="Sexo",
        choices=Cliente.SEXO,
    )
    telefono = forms.CharField(label="Telefono")
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = Cliente
        fields = [
            "nombre",
            "apellido",
            "fecha_nacimiento",
            "dni",
            "sexo",
            "telefono",
            "direccion",
            "avatar"
        ]



class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(required=True, label="Email")
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
