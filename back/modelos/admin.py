from django.contrib import admin
from .models import Modelo, Carroceria, Parte

class ParteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Parte, ParteAdmin)

class CarroceriaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carroceria, CarroceriaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    pass

admin.site.register(Modelo, ModeloAdmin)
