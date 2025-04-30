import os
from django.db import models

class Ropa(models.Model):
    """
    Modelo para la ropa de la tienda.
    """

    TALLES = (
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
    ) 
    nombre = models.CharField(max_length=100)  # Ej: Pantalón
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=20, choices=TALLES)
    imagen = models.ImageField(upload_to='ropa/', blank=True, null=True, )
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.color} - Talla {self.talla}"
    
    def delete(self, *args, **kwargs):
        """
        Borramos la imagen del producto cuando se elimina el objeto.
        """
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)