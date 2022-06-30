from django.shortcuts import redirect, render
from .form import *
from django.contrib.auth import login, logout, authenticate
from .models import *

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

def ingresar(request):
    data = {"mesg": "", "form": formulario_ingresar()}
    user=Usuario
    if request.method == "POST":
        form = formulario_ingresar(request.POST)
        if form.is_valid:
            try:
                v_rutUsuario = request.POST.get("rutUser")
                password = request.POST.get("passw")
                v_user=Usuario.objects.get(rutUsuario = v_rutUsuario)
                print( CategoriaUsuario.objects.filter(nombreCategriaUsuario= "usuario"))
                if v_user.contraseñaUsuario == password:
                    print(Usuario.categoria)
                    if v_user.categoria == CategoriaUsuario.objects.get(nombreCategriaUsuario= "usuario"):
                        print("a")
                        return redirect(inicio_como_cliente)
                    elif  v_user.categoria == CategoriaUsuario.objects.get(nombreCategriaUsuario= "administrador"):
                        print("b")
                        return redirect(inicio_como_administrador)
            except:
                data["mesg"] = "nombre de usuario o contraseña incorrecta"
    return render(request, "ingresar.html", data)

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

    if request.method == "POST": #listo
        form = mantenedorBodega(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = mantenedorBodega()
    return render(request, 'mantenedor_de_bodega.html', {"form": form, "p": p})

def mantenedor_de_productos(request, idProducto, action = "ins"):
    p_s = Producto.objects.get(idProduco = idProducto) #confirmar si el formulario en html funciona
    p = Producto.objects.all()

    data = {"mesg": "", "form": ficha_producto, "action": action, "id": idProducto}

    if action == 'ins':
        if request.method == "POST":
            form = mantenerdorProducto(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "el producto fue agregado"
                except:
                    data["mesg"] = "no se ha agregado"

    elif action == 'upd':
        objeto = Producto.objects.get(idProduco=idProducto)
        if request.method == "POST":
            form = mantenerdorProducto(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "el producto se actualizo"
        data["form"] = mantenerdorProducto(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(idProduco=idProducto).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(mantenedor_de_productos, action='ins', idProduco = '-1')
        except:
            data["mesg"] = "el producto no existia"

    data["list"] = Producto.objects.all().order_by('idProduco')
    return render(request, "mantenedor_de_productos.html", data)

def mantenedor_de_usuarios(request): #confirmar si el formulario en html funciona
    u = Usuario.objects.all()
    """
    hacer que los datos se agreguen / actualizen
    """
    if request.method == "POST":
        form = formuario_registrar(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = formuario_registrar()
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
    """
    que se guarde la informacion
    """
    if request.method == "POST":
        form = formuario_registrar(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            form.save()
            return redirect("/ingresar")
    else:
        form = formuario_registrar()
    return render(request, 'registrarse.html', {"form": form})
