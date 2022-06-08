from django.db import models

# Create your models here.


#modelo de categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nombreCategoria

#modelo de producto
class Producto(models.Model):
    idProduco = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, models.CASCADE, blank=False, null=False)
    nombreProducto = models.CharField(max_length=100, blank=False, null=False)
    precioProducto = models.IntegerField(blank=False, null=False)
    descripcionProducto = models.CharField(max_length=300, blank=False, null=False)
    disponibilidadProducto = models.BooleanField(blank=False, null=False)