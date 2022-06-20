from django import forms
from django.forms import ModelForm
from .models import Producto

class formulario_ingresar(forms.Form):
    uName = forms.CharField(max_length=50)
    passw = forms.CharField(max_length=50)

class formuario_registrar(forms.Form):
    rut = forms.CharField(max_length=10)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    correo = forms.EmailField()
    direccion = forms.CharField(max_length=500)
    suscripcion = forms.BooleanField()
    contraseña = forms.CharField(max_length=50)
    contraseñaRepetida = forms.CharField(max_length=50)
    imagen = forms.ImageField()

class mantenerdorProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ["imagenProducto", "imagenProducto", "categoria", "nombreProducto", "precioProducto", "descripcionProducto", "disponibilidadProducto"]

class mantenedorUsuario(forms.Form):
    choices = [("1", "cliente"), ("2", "admin")]
    idUsuario = forms.CharField(max_length=100)
    tipoUsuario = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    rutUsusario = forms.CharField(max_length=10)
    nombreUsuario = forms.CharField(max_length=50)
    apellidoUsuario = forms.CharField(max_length=50)
    direccionUsuario = forms.CharField(max_length=500, widget=forms.Textarea)
    SuscripcionUsuario = forms.BooleanField()
    contrasenaUsuario = forms.CharField(max_length=50, min_length=10)
    imagenUsuario = forms.FileField()

class mantenedorBodega(forms.Form):
    choiceCategoria = [("1", "perro"), ("2", "gato")]
    idBodega = forms.IntegerField()
    categoriaBodega = forms.ChoiceField()
    cantidadBodega = forms.IntegerField()