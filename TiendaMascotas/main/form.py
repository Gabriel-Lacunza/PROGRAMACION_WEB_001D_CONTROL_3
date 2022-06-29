from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import *

class formulario_ingresar(forms.Form):
    rUSer = forms.CharField(max_length=50)
    passw = forms.CharField(max_length=50)
    class Meta:
        fields =["rutUsuario","contraseña"]

class formuario_registrar(ModelForm):
    class Meta:
        model = Usuario
        fields = ["idUsuario","categoria", "rutUsuario", "nombreUsuario", "apellidoUsuario", "direccionUsusario", "suscripcionUsusario", "contraseñaUsuario", "imagenUsuario"]

class mantenerdorProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ["imagenProducto", "imagenProducto", "categoria", "nombreProducto", "precioProducto", "descripcionProducto", "disponibilidadProducto"]

class mantenedorBodega(forms.Form):
    class Meta:
        model = Producto
        fields = ["idProductoBodega", "idProducto", "idDetalleFactura"]
