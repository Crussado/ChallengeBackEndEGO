from django.contrib import admin
from .models import Concesionario

class ConcesionarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Concesionario, ConcesionarioAdmin)
