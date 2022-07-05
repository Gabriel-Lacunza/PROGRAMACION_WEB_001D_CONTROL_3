from email.policy import default
from django import forms
from django.forms import ModelForm, fields, Form
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nomProducto', 'descripcion', 'precio','porcDesctoSubscriptor','porcDesctoOferta','imagen', 'categoria']

class BodegaForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nomProducto','categoria', 'cantidad' ]

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.CharField(required=True)
    rutUsuario = forms.CharField(required=True)
    direccionUsusario = forms.CharField(required=True)
    suscripcionUsusario = forms.BooleanField(required=False)
    imagenUsuario = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'rutUsuario',
                'direccionUsusario',
                'suscripcionUsusario',
                'imagenUsuario',
            ]

class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class PerfilUsuarioForm(Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombres")
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    email = forms.CharField(max_length=254, required=True, label="Correo")
    rutUsuario = forms.CharField(max_length=80, required=False, label="Rut")
    direccionUsusario = forms.CharField(max_length=80, required=False, label="Dirección")

    class Meta:
        fields = '__all__'

class Usuarios(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.CharField(required=True)
    rutUsuario = forms.CharField(required=True)
    direccionUsusario = forms.CharField(required=True)
    suscripcionUsusario = forms.BooleanField(required=False)
    imagenUsuario = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'rutUsuario',
                'direccionUsusario',
                'suscripcionUsusario',
                'imagenUsuario',
            ]