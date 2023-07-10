from django.contrib import admin
from.models import Coches

# Register your models here.
from .models import Coches


@admin.register(Coches)
class CochesAdmin(admin.ModelAdmin):
    ...
