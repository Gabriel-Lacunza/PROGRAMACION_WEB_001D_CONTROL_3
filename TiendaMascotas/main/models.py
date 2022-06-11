from django.db import models
from django.forms import IntegerField

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

class CategoriaUsuario(models.Model):
    idCategoriaUsusario = models.IntegerField(primary_key=True)
    nombreCategriaUsuario = models.CharField(max_length=80, blank=False, null=False)

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(CategoriaUsuario, models.CASCADE, blank=False, null=False)
    rutUsuario = models.CharField(max_length=10, unique=True)
    nombreUsuario = models.CharField(max_length=50) 
    direccionUsusario = models.CharField(max_length=100)
    suscripcionUsusario = models.BooleanField()
    contraseñaUsuario = models.CharField(max_length=50)
    imagenUsuario = models.FileField()