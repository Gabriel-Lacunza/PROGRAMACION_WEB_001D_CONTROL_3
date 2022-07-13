from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import RemoteUserAuthentication
from rest_framework.decorators import permission_classes
from .models import *
from .forms import *
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate


# Create your views here.
 
def home(request):
    model = Producto
    data = {"list": Producto.objects.all().order_by('nomProducto')}
    prodis = {"list": Producto.objects.filter(cantidad__gte =1).order_by('nomProducto')}
    if Producto.objects.filter(cantidad__gte =1):
        return render(request, "core/inicio_cliente.html", prodis)
    else:
        return render(request, "core/inicio_cliente.html")

""" def producto_tienda(request):
    data = {"list": Producto.objects.all().order_by('nomProducto')}
    return render(request, "core/inicio_anonimo.html", data)
"""
def inicio_cliente(request):
    model = Producto
    data = {"list": Producto.objects.all().order_by('nomProducto')}
    prodis = {"list": Producto.objects.filter(cantidad__gte =1).order_by('nomProducto')}
    if Producto.objects.filter(cantidad__gte =1):
        return render(request, "core/inicio_cliente.html", prodis)
    else:
        return render(request, "core/inicio_cliente.html")

def iniciar_sesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            admin= request.POST.get("is_staff")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.is_staff:
                        login(request, user)
                        return redirect("mainAdministrador")
                    else:
                        login(request, user)
                        return redirect("inicio_cliente")
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "core/login.html", data)

def cerrar_sesion(request):
    logout(request)
    return redirect(home)

def mainAdministrador(request):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)
    data = {"list": Producto.objects.all().order_by('idProducto')}
    return render(request, "core/main_administrador.html", data)

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user= form.save()
            rut = request.POST.get("rutUsuario")
            direccion = request.POST.get("direccionUsusario")
            susbcripcion = request.POST.get("suscripcionUsusario")
            imagen = request.POST.get("imagenUsuario")
            PerfilUsuario.objects.update_or_create(user=user,rutUsuario=rut,direccionUsusario=direccion,imagenUsuario=imagen)
            return redirect(iniciar_sesion)
    form = RegistroForm()
    return render(request, "core/registro.html", context={'form': form})

def producto_ficha(request, id):
    producto = Producto.objects.get(idProducto=id)
    data = {"producto":  producto}
    return render(request, "core/ficha_producto_anon.html", data)

def sobre_nosotros(request):
    return render(request, "core/sobre_nosotros.html")

def maestro_producto(request, action, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}
 
    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El Producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos Productos con el mismo ID!"
 
    elif action == 'upd':
        objeto = Producto.objects.get(idProducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
        form
        data["form"] = ProductoForm(instance=objeto)
 
    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El Producto fue eliminado correctamente!"
            return redirect(Producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Producto ya estaba eliminado!"
 
    data["list"] = Producto.objects.all().order_by('idProducto')
    return render(request, "core/maestro_producto.html", data)

def maestro_bodega(request, action, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)
    data = {"mesg": "", "form": BodegaForm, "action": action, "id": id}
    if action == 'upd':
        objeto = Producto.objects.get(idProducto=id)
        if request.method == "POST":
            form = BodegaForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
        data["form"] = BodegaForm(instance=objeto)
 
    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El Producto fue eliminado correctamente!"
            return redirect(Producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Producto ya estaba eliminado!"
 
    data["list"] = Producto.objects.all().order_by('idProducto')
    return render(request, "core/maestro_bodega.html", data)

def maestro_usuario(request,action, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)

    data = {"mesg": "", "form": Usuarios, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = MantUsuarioForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El Usuario fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos Usuarios con el mismo ID!"
    elif action == 'upd':
        objeto = PerfilUsuario.objects.get(id=id)
        if request.method == "POST":
            form = Usuarios(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
        data["form"] = Usuarios(instance=objeto)
    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El Producto fue eliminado correctamente!"
            return redirect(Producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Producto ya estaba eliminado!"
    data["list"] = PerfilUsuario.objects.all().order_by('user_id')
    return render(request, "core/maestro_usuario.html", data)

def mi_perfil(request):
    data = {"mesg": "", "form": PerfilUsuarioForm}
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.save()
            perfil = PerfilUsuario.objects.get(user=user)
            perfil.rutUsuario = request.POST.get("rutUsuario")
            perfil.direccionUsusario = request.POST.get("direccionUsusario")
            perfil.save()
            data["mesg"] = "¡Sus datos fueron actualizados correctamente!"

    perfil = PerfilUsuario.objects.get(user=request.user)
    form = PerfilUsuarioForm()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['email'].initial = request.user.email
    form.fields['rutUsuario'].initial = perfil.rutUsuario
    form.fields['direccionUsusario'].initial = perfil.direccionUsusario
    data["form"] = form
    return render(request, "core/mi_perfil.html", data)

def registro_ventas(request):
    data = {"mesg": ""}

    data["list"] = Factura.objects.all().order_by('id')
    return render(request, "core/registro_ventas.html", data)

def detalle_factura(request, id):
    detalle = DetalleFactura.objects.get(factura_id=id)
    data = {"detalle":  detalle}
    return render(request, "core/detalle_factura.html", data)

def mis_compras(request, id):
    factura = Factura.objects.filter(usuario_id=id)
    detalle = DetalleFactura.objects.filter(factura_id=factura)
    data = {"list": Factura.objects.filter(usuario_id=id), "detalle":detalle}
    return render(request, "core/mis_compras.html", data)