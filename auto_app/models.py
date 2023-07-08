from django.db import models

# Create your models here.
class Coches(models.Model):
    nombre = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(null=False, blank=False)
    abv = models.FloatField(null=True, blank=True)
    
class Meta:
    db_table = "autos_table"
    
def __str__(self):
    return f"El auto: {self.nombre}, Rating {self.abv}"

def get_fields(self):
    return[
        (field.verbose.name, field.value_from_object(self))
        for field in self.__clss__.meta.fields[1:]
    ]    
    
    