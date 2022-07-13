from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *
from .views import *
from datetime import datetime

def comprar_producto (request,id):
    cont= 0
    cont = cont + 1
    if request.method == "GET":
        user = request.user.id
        perfil = PerfilUsuario.objects.get(user=user)
        producto = Producto.objects.get(idProducto=id)
        precio = producto.precio
        direccion = perfil.direccionUsusario
        total = producto.precio
        nroitem = producto.idProducto
        fecha = datetime.today().strftime('%Y-%m-%d')
        Factura.objects.create(usuario_id=user,fecha=fecha)
        
        DetalleFactura.objects.create(factura_id=1,nroItem=nroitem,precio=total,direccionUsusario=direccion,precioFinal=total)
        return render(request, "core/registro.html")
    else:
        return render(request, "core/login.html")



def compra_exitosa(request,id):
    if request.method == "GET":
        user = User.objects.get(user)
        perfil = PerfilUsuario.objects.get(user=user)
        producto = PerfilUsuario.objects.get(idProducto=id)
        form = PerfilUsuarioForm()

        context = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "rut": perfil.rut,
            "direccion": perfil.direccion,
        }

        return render(request, "core/pago_exitoso.html", context)
    else:
        return redirect(home)