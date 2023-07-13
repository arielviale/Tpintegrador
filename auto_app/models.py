from django.db import models

class Coche(models.Model):
    nombre = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(null=False, blank=False)
    abv = models.FloatField(null=True, blank=True)
    
    class Meta:
        db_table = "autos_table"
    
    def __str__(self):
        return f"El auto: {self.nombre}, Rating {self.abv}"

    def get_fields(self):
        return [
            (field.verbose_name, getattr(self, field.name))
            for field in self._meta.fields[1:]
        ]
 

class Venta(models.Model):
    coche = models.ForeignKey("auto_app.Coche", on_delete=models.CASCADE, related_name="ventas")
    fecha = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "ventas_table"

    def __str__(self):
        return f"Venta de {self.coche} por {self.precio}"
