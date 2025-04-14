# models.py
from django.db import models

class Ropa(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: Pantalón
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} - {self.color} - Talla {self.talla}"