from django.contrib  import admin
from.models          import Coche



@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    ...
