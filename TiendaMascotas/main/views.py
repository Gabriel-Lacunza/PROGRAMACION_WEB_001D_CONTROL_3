from django.shortcuts import render

# Create your views here.

def adminTienda(request):
    return render(request, 'administrar_tienda.html', {})

def carritoCompra(request):
    return render(request, 'carrito_de_compras.html', {})

def detalleFactura(request):
    return render(request, 'detalle_factura.html', {})

def fichaProducto(request):
    return render(request, 'administrar_tienda.html', {})

def index(request):
    return render(request, 'index.html', {})

def inicioCli(request):
    return render(request, 'inicio_cliente.html', {})

def inventario(request):
    return render(request, 'inventario.html', {})

def login(request):
    return render(request, 'login.html', {})

def maestroProducto(request):
    return render(request, 'maestro_producto.html', {})

def maestroUsuario(request):
    return render(request, 'maestro_usuario.html', {})

def mainAdmin(request):
    return render(request, 'main_administrador.html', {})

def misCompras(request):
    return render(request, 'mis_compras.html', {})

def registroVentas(request):
    return render(request, 'registro_ventas.html', {})

def registro(request):
    return render(request, 'registro.html', {})

def sobreNos(request):
    return render(request, 'sobre_nosotros.html', {})