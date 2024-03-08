from django.db import models
from django.core.validators import MinValueValidator

from decimal import Decimal

# Create your models here.
class Extra(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    tipo = models.BooleanField(choices=[(True, 'Servicio'), (False, 'Accesorio')])

    def __str__(self):
        return str(self.nombre)
