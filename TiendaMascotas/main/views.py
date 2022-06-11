from django.http import HttpResponse
from django.shortcuts import render
from .form import *

# Create your views here.
listaProductos = []

def adminTienda(request):
    return render(request, 'administrar_tienda.html', {})

def carritoCompra(request):
    """
    agregar el append a listaProductos al presionar el boton "agregar al carrito"
    """
    return render(request, 'carrito_de_compras.html', {})

def detalleFactura(request):
    """
    imprimir lo que listaProductos tenga
    """
    return render(request, 'detalle_factura.html', {})

def fichaProducto(request):
    """
    imprimir el producto seleccionado (por ende agregar requisito para filtrar) y agregar el producto a listaProducto
    """
    return render(request, 'administrar_tienda.html', {})

def index(request):
    """
    que se imprima los productos en la base da datos
    """
    return render(request, 'index.html', {})

def inicioCli(request):
    """
    que se imprima los productos en la base da datos
    """
    return render(request, 'inicio_cliente.html', {})

def inventario(request):
    """
    que se agreguen / actualizen los datos, 
    ademas de que se muestren en la lista de abajo
    agregar formulario de inventario
    """
    return render(request, 'inventario.html', {})

def login(request):
    """
    que se valide la llegada de un usuario
    agregar formulario de login
    """
    return render(request, 'login.html', {})

def maestroProducto(request):
    form = mantenerdorProducto
    """
    que se muestren los productos en la lista de abajo
    que se agreguen / actualicen los datos
    """
    return render(request, 'maestro_producto.html', {"form": form})

def maestroUsuario(request):
    form = mantenedorUsuario
    """
    que la infromacion se muestre en la lista de abajo
    que los datos se agreguen / actualizen
    """
    return render(request, 'maestro_usuario.html', {"form": form})

def mainAdmin(request):
    """
    que el boton "editar" te lleve a su maestroProducto, con los datos ya cargados
    """
    return render(request, 'main_administrador.html', {})

def misCompras(request):
    """
    ver como hacer le registro de compras
    """
    return render(request, 'mis_compras.html', {})

def registroVentas(request):
    """
    ver como hacer la pagina
    """
    return render(request, 'registro_ventas.html', {})

def registro(request):
    form = registrar
    """
    que se guarde la informacion
    """
    return render(request, 'registro.html', {"form": form})

def sobreNos(request):
    return render(request, 'sobre_nosotros.html', {})