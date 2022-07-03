from xml.dom.minidom import Identified
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


#modelo de categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nombreCategoria

#modelo de producto
class Producto(models.Model):
    imagenProducto = models.ImageField(upload_to="media/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    idProduco = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, models.CASCADE, blank=False, null=False)
    nombreProducto = models.CharField(max_length=100, blank=False, null=False)
    precioProducto = models.IntegerField(blank=False, null=False)
    descripcionProducto = models.CharField(max_length=300, blank=False, null=False, default="")
    disponibilidadProducto = models.BooleanField(blank=False, null=False, default=False)
    porcentageSuscripcion = models.IntegerField(blank=False, null=False, default=0)
    procentageOferta = models.IntegerField(blank=False, null=False, default=0)
    
    def __str__(self) -> str:
        return self.nombreProducto


class CategoriaUsuario(models.Model):
    idCategoriaUsusario = models.IntegerField(primary_key=True)
    nombreCategriaUsuario = models.CharField(max_length=80, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.nombreCategriaUsuario

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(CategoriaUsuario, models.CASCADE, default=2)
    rutUsuario = models.CharField(max_length=10, unique=True)
    nombreUsuario = models.CharField(max_length=50) 
    apellidoUsuario = models.CharField(max_length=50, default="")
    direccionUsusario = models.CharField(max_length=100)
    suscripcionUsusario = models.BooleanField(default=False)
    contraseñaUsuario = models.CharField(max_length=50)
    imagenUsuario = models.ImageField(upload_to="media/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")

    def __str__(self):
        return self.nombreUsuario

"""
class Usuario(AbstractBaseUser):
    idUsuario = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=1)
    rutUsuario = models.CharField(max_length=10, unique=True)
    nombreUsuario = models.CharField(max_length=50) 
    apellidoUsuario = models.CharField(max_length=50, default="")
    direccionUsusario = models.CharField(max_length=100)
    suscripcionUsusario = models.BooleanField(default=False)
    contraseñaUsuario = models.CharField(max_length=50)
    imagenUsuario = models.ImageField(upload_to="media/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")

    USERNAME_FIELD = 'rutUsuario'
    REQUIRED_FIELDS = ['nombreUsuario', 'apellidoUsuario']

    def __str__(self):
        return f'{self.nombreUsuario}, {self.apellidoUsuario}'
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.categoria
        """
class factura(models.Model):
    idFactura = models.IntegerField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    nroFactura = models.IntegerField(null=False)
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    estadoFactura = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.idFactura} - {self.idUsuario}"

class detalleFactura(models.Model):
    idDetalleFactura = models.IntegerField(primary_key=True)
    idFactura = models.IntegerField(models.ForeignKey(factura, on_delete=models.CASCADE))
    nroItem = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return self.idDetalleFactura

class productoBodega(models.Model):
    idProductoBodega = models.IntegerField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idDetalleFactura = models.ForeignKey(detalleFactura, on_delete=models.CASCADE)

