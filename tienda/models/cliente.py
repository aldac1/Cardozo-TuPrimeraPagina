# models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"