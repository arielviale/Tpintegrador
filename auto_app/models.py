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
        