from django.shortcuts import redirect, render
from .form import *
from .models import Producto, Usuario

# Create your views here.
listaProductos = []
totalPedido = 0

def adminTienda(request):
    return render(request, 'administrar_tienda.html', {})

def carritoCompra(request):
    lista = listaProductos
    t = totalPedido
    return render(request, 'carrito_de_compras.html', {"lista": lista, "total": t})

def detalleFactura(request):
    lista = listaProductos
    """
    imprimir lo que listaProductos tenga
    """
    return render(request, 'detalle_factura.html', {"lista": lista})

def fichaProducto(request, idProduco):
    p = Producto.objects.get(idProduco = idProduco)
    formu = pedidos
    total = totalPedido

    if request.method == "POST":
        formu = pedidos(request.POST)
        if formu.is_valid():
            c = formu.cleaned_data["cantidad"]
            listaProductos.append([p.categoria.nombreCategoria, p.nombreProducto, p.precioProducto*c])
            total += p.precioProducto*c
            print(listaProductos)
        else:
            formu = pedidos
    return render(request, 'ficha_producto_anon.html', {"p": p, "form": formu})

def index(request):
    prd = Producto.objects.all()
    return render(request, 'index.html', {"prd": prd})

def inicioCli(request):
    prd = Producto.objects.all()
    return render(request, 'inicio_cliente.html', {"prd": prd})

def inventario(request):
    p = Producto.objects.all()

    if request.method == "POST":
        form = mantenerdorProducto(request.POST)
        if form.is_valid():
            i = form.cleaned_data["idProducto"]
            c = form.cleaned_data["categoriaProducto"]
            n = form.cleaned_data["nombreProducto"]
            can = form.cleaned_data["cantidadProducto"]
            im = form.cleaned_data["imagenProducto"]
            pr = Producto(imagenProducto = im, idProduco = i, categoria = c,  nombreProducto = n, cantidadProducto = can)
            pr.save
        else:
            form = mantenerdorProducto
    return render(request, 'inventario.html', {"form": form, "p": p})

def login(request):
    form = log

    if request.method == "post":
        if form.is_valid:
            return redirect(to=inicioCli)
    """
    que se valide la llegada de un usuario
    """
    return render(request, 'login.html', {"form": form})

def maestroProducto(request):
    form = mantenerdorProducto
    p = Producto.objects.all()

    if request.method == "POST":
        form = mantenerdorProducto(request.POST)
        if form.is_valid():
            i = form.cleaned_data["idProducto"]
            c = form.cleaned_data["categoriaProducto"]
            n = form.cleaned_data["nombreProducto"]
            d = form.cleaned_data["descripcionProducto"]
            pre = form.cleaned_data["precioProducto"]
            desS = form.cleaned_data["descuentoSuscriptor"]
            desO = form.cleaned_data["descuentoOferta"]
            im = form.cleaned_data["imagenProducto"]
            pr = Producto(imagenProducto = im, idProduco = i, categoria = c,  nombreProducto = n, descripcionProducto = d, precioProducto = pre, descuentoSuscriptor = desS, descuentoOferta = desO)
            pr.save
        else:
            form = mantenerdorProducto
    """
    pendiente
    que se agreguen / actualicen los datos
    """
    return render(request, 'maestro_producto.html', {"form": form, "p": p})

def maestroUsuario(request):
    form = mantenedorUsuario
    u = Usuario.objects.all()
    """
    que los datos se agreguen / actualizen
    """
    return render(request, 'maestro_usuario.html', {"form": form, "u": u})

def mainAdmin(request):
    p = Producto.objects.all()
    """
    que el boton "editar" te lleve a su maestroProducto, con los datos ya cargados
    """
    return render(request, 'main_administrador.html', {"p": p})

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