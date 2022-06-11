from django import forms

class login(forms.Form):
    nombreUsuario = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=50)

class registrar(forms.Form):
    rut = forms.CharField(max_length=10)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    correo = forms.EmailField()
    direccion = forms.CharField(max_length=500)
    suscripcion = forms.BooleanField()
    contraseña = forms.CharField(max_length=50)
    contraseñaRepetida = forms.CharField(max_length=50)
    imagen = forms.FileField()

class mantenerdorProducto(forms.Form):
    idProducto = forms.CharField(max_length=100)
    categoriaProducto = forms.ChoiceField()
    nombreProducto = forms.CharField(max_length=100)
    descripcionProducto = forms.CharField(max_length=500)
    precioProducto = forms.IntegerField()
    descuentoSuscriptor = forms.IntegerField(max_value=100)
    descuentoOferta = forms.IntegerField(max_value=100)
    imgenProducto = forms.FileField()

class mantenedorUsuario(forms.Form):
    choices = [("1", "cliente"), ("2", "admin")]
    idUsuario = forms.CharField(max_length=100)
    tipoUsuario = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    rutUsusario = forms.CharField(max_length=10)
    nombreUsuario = forms.CharField(max_length=50)
    direccionUsuario = forms.CharField(max_length=500)
    SuscripcionUsuario = forms.BooleanField()
    contrasenaUsuario = forms.CharField(max_length=50, min_length=10)
    imagenUsuario = forms.FileField()

