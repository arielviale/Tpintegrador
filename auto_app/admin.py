from django.contrib import admin

# Register your models here.
from .models import Coches


@admin.register(Coches)
class CochesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion del Coche', {'fields': ['marca', 'modelo', 'anio']}),
        ('Precio y Stock', {'fields': ['precio', 'stock']}),
    ]
