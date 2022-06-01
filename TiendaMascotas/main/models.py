from django.db import models

# Create your models here.

"""
#modelo de categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="id de la categoria")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nombreCategoria

#class Vehiculo(models.Model):
"""