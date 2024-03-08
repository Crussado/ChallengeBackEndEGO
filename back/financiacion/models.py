from django.db import models

# Create your models here.
class TipoFinanciacion(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tipo)

class Financiacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    tipo = models.ForeignKey(TipoFinanciacion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

