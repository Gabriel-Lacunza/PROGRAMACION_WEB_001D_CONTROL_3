from django import forms

class log(forms.Form):
    uName = forms.CharField(max_length=50)
    passw = forms.CharField(max_length=50)

class registrar(forms.Form):
    rut = forms.CharField(max_length=10)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    correo = forms.EmailField()
    direccion = forms.CharField(max_length=500)
    suscripcion = forms.BooleanField()
    contraseña = forms.CharField(max_length=50)
    contraseñaRepetida = forms.CharField(max_length=50)
    imagen = forms.ImageField()

class mantenerdorProducto(forms.Form):
    choices = [("1", "perro"), ("2", "gato")]
    idProducto = forms.CharField(max_length=100)
    categoriaProducto = forms.ChoiceField(choices=choices)
    nombreProducto = forms.CharField(max_length=100)
    descripcionProducto = forms.CharField(max_length=500)
    precioProducto = forms.IntegerField()
    descuentoSuscriptor = forms.IntegerField(max_value=100)
    descuentoOferta = forms.IntegerField(max_value=100)
    imgenProducto = forms.FileField()
    cantidadProducto = forms.IntegerField()
    imagenProducto = forms.ImageField()

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

class pedidos(forms.Form):
    cantidad = forms.IntegerField()