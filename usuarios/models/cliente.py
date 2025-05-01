# models.py
from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    SEXO = [('M', 'Masculino'), ('F', 'Femenino')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(blank=True, null=True, max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
