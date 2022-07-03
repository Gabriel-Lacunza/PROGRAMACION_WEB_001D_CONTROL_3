from dataclasses import field
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class formulario_ingresar(forms.Form):
    rutUser = forms.CharField(max_length=50)
    passw = forms.CharField(widget=forms.PasswordInput(), max_length=50)
    class Meta:
        fields =["rutUser","passw"]

class formuario_registrar(ModelForm):
    class Meta:
        model = Usuario
        fields = ["idUsuario", "rutUsuario", "nombreUsuario", "apellidoUsuario", "direccionUsusario", "suscripcionUsusario", "contraseñaUsuario", "imagenUsuario"]

class M_usuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ["rutUsuario", "nombreUsuario", "apellidoUsuario", "direccionUsusario", "suscripcionUsusario", "contraseñaUsuario", "imagenUsuario"]

class mantenerdorProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ["imagenProducto", "idProduco", "categoria", "nombreProducto", "precioProducto", "descripcionProducto", "disponibilidadProducto"]

class mantenedorBodega(forms.Form):
    class Meta:
        model = Producto
        fields = ["idProductoBodega", "idProducto", "idDetalleFactura"]
