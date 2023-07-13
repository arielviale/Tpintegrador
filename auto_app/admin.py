from django.contrib import admin
from.models import Coche

# Register your models here.
from .models import Coche


@admin.register(Coche)
class CochesAdmin(admin.ModelAdmin):
    ...
