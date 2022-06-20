from django.shortcuts import redirect, render
from .form import *
from .models import Producto, Usuario

# Create your views here.
listaProductos = []
totalPedido = 0

def carrito_de_compras(request): 
    """
    falta que la pagina calcule el total por producto
    """
    lista = listaProductos
    t = totalPedido
    return render(request, 'carrito_de_compras.html', {"lista": lista, "total": t})

def detalle_factura(request):
    lista = listaProductos
    """
    imprimir lo que listaProductos tenga
    """
    return render(request, 'detalle_factura.html', {"lista": lista})

def ficha_producto(request, idProduco): #listo
    p = Producto.objects.get(idProduco = idProduco)
    return render(request, 'ficha_producto.html', {"p": p})

def historial_de_ventas(request):
    """
    ver como hacer la pagina
    """
    return render(request, 'historial_de_ventas.html', {})

def ingresar(request): #arreglar formulario en html
    form = formulario_ingresar

    if request.method == "post":
        if form.is_valid:
            return redirect(to=inicio_como_cliente)
    """
    que se valide la llegada de un usuario
    confirmar que te redirija a la pagina inicio cli
    """
    return render(request, 'ingresar.html', {"form": form})

def inicio_como_administrador(request):
    p = Producto.objects.all()
    """
    que el boton "editar" te lleve a su maestroProducto, con los datos ya cargados
    """
    return render(request, 'inicio_como_administrador.html', {"p": p})

def inicio_como_cliente(request): #listo
    prd = Producto.objects.all()
    return render(request, 'inicio_como_cliente.html', {"prd": prd})

def inicio_usuario_anonimo(request): #listo
    prd = Producto.objects.all()
    return render(request, 'inicio_usuario_anonimo.html', {"prd": prd})

def mantenedor_de_bodega(request): #confirmar si el formulario en html funciona
    """
    hacer que rellene la base de datos
    """
    p = Producto.objects.all()

    if request.method == "POST":
        form = mantenedorBodega(request.POST)
        
        if form.is_valid():
            i = form.cleaned_data["idProducto"]
            c = form.cleaned_data["categoriaProducto"]
            n = form.cleaned_data["nombreProducto"]
            can = form.cleaned_data["cantidadProducto"]
            im = form.cleaned_data["imagenProducto"]
            d = form.cleaned_data["disponibilidad"]
            pr = Producto(imagenProducto = im, idProduco = i, categoria = c,  nombreProducto = n, cantidadProducto = can, disponibilidadProducto = d)
            pr.save()
    else:
        form = mantenedorBodega()
    return render(request, 'mantenedor_de_bodega.html', {"form": form, "p": p})

def mantenedor_de_productos(request): #confirmar si el formulario en html funciona
    p = Producto.objects.all()

    if request.method == "POST": #listo
        form = mantenerdorProducto(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = mantenerdorProducto()
    return render(request, 'mantenedor_de_productos.html', {"form": form, "p": p})

def mantenedor_de_usuarios(request): #confirmar si el formulario en html funciona
    form = mantenedorUsuario
    u = Usuario.objects.all()
    """
    hacer que los datos se agreguen / actualizen
    """
    return render(request, 'mantenedor_de_usuarios.html', {"form": form, "u": u})

def menu_de_administracion(request): #listo
    return render(request, 'menu_de_administracion.html', {})

def mis_compras(request):
    """
    ver como hacer le registro de compras
    """
    return render(request, 'mis_compras.html', {})

def nosotros(request): #listo
    return render(request, 'nosotros.html', {})

def registrarse(request): #arreglar formulario en html
    form = formuario_registrar
    """
    que se guarde la informacion
    """
    return render(request, 'registrarse.html', {"form": form})
