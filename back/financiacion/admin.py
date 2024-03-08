from django.contrib import admin
from .models import TipoFinanciacion, Financiacion

# Register your models here.
class FinanciacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Financiacion, FinanciacionAdmin)

class TipoFinanciacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoFinanciacion, TipoFinanciacionAdmin)
