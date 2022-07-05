from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")
 
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id Producto")
    nomProducto = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre Producto")
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")
    porcDesctoSubscriptor = models.IntegerField(blank=False, null=False, default=0,verbose_name="Porcentaje Descuento Suscriptor")
    porcDesctoOferta = models.IntegerField(blank=False, null=False, default=0,verbose_name="Porcentaje Descuento Oferta")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen Producto")
    cantidad= models.IntegerField(blank=False, null=False, default=0,verbose_name="Cantidad")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
 
    def __str__(self):
        return self.nomProducto

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    rutUsuario = models.CharField(max_length=15, unique=True)
    direccionUsusario = models.CharField(max_length=300, blank=False, null=False, verbose_name="Direccion Usuario")
    suscripcionUsusario = models.BooleanField(default=False,blank=False, null=False, verbose_name="Suscriptor")
    imagenUsuario = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen Usuario")
    
    def __str__(self):
        return f"{self.user.username}  {self.user.first_name} {self.user.last_name} {self.user.email}"

class Factura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nroFactura = models.IntegerField(blank=False, null=False, verbose_name="Nro Item")   
    fecha = models.DateField(blank=False, null=False, verbose_name="Fecha Factura")
    estado = models.CharField(max_length=1, default="B",blank=False, null=False, verbose_name="Fecha Factura")

    def __str__(self):
        return self.id

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nroItem = models.IntegerField(blank=False, null=False, verbose_name="Nro Factura")
    precio = models.IntegerField(blank=False, null=False, verbose_name="Precio")
    direccionUsusario = models.CharField(max_length=300, blank=False, null=False, verbose_name="Direccion Usuario")
    suscripcionUsusario = models.BooleanField(default=False,blank=False, null=False, verbose_name="Suscriptor")
    precioFinal = models.IntegerField(blank=False, null=False, verbose_name="Precio Final")

    def __str__(self):
        return self.id

