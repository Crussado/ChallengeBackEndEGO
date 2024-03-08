from django.db import models

# Create your models here.
class Concesionario(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)
