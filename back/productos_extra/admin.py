from django.contrib import admin
from .models import Extra

class ExtraAdmin(admin.ModelAdmin):
    pass

admin.site.register(Extra, ExtraAdmin)

