from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from decimal import Decimal

class Carroceria(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tipo)

class Parte(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    url_img = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    precio = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    anio = models.IntegerField(
        validators=[
            MinValueValidator(1900, message="El año debe ser mayor o igual a 1900."),
            MaxValueValidator(2100, message="El año debe ser menor o igual a 2100.")
        ]
    )
    url_img = models.CharField(max_length=50, blank=True, null=True)
    resumen = models.CharField(max_length=150, blank=True, null=True)
    carroceria = models.ForeignKey(Carroceria, on_delete=models.CASCADE)
    partes = models.ManyToManyField(Parte, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.marca}'
