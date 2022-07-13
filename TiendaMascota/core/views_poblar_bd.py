from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Producto, Categoria, PerfilUsuario
from .views import *

def poblar_bd(request):
    try:
        Producto.objects.all().delete()
        print("Tabla Producto fue truncada.")
        Categoria.objects.all().delete()
        print("Tabla Categoria fue truncada.")
        print("Iniciar poblamiento de tabla Categoria.")
        Categoria.objects.create(idCategoria=1, nombreCategoria="Perros")
        Categoria.objects.create(idCategoria=2, nombreCategoria="Gatos")
        print("Tabla Categoria fue poblada.")
    except Exception as err:
        print(f"Error al poblar tabla Categoria: {err}")
    try:
        print("Iniciar poblamiento de tabla Producto.")
        Producto.objects.create(idProducto="1", nomProducto='Bakery Chicken Puppy', descripcion="Alimento completo para cachorros de razas medianas y grandes", precio=53990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/alimentoP1.jpg", cantidad=1 , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="2", nomProducto='Wellness Core Dog Original', descripcion="Alimento completo para perros, sabor a pavo y pollo", precio=59990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/alimentoP2.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="3", nomProducto='Dogxtreme Adult Salmon & Rice', descripcion="Para una mejora visible del pelaje, elaborado con salmon", precio=31990 , porcDesctoSubscriptor= 0, porcDesctoOferta=0, imagen="images/alimentoP3.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="4", nomProducto='Salvaje Cachorro Pollo', descripcion="Alimento especial para cachorros con ingredientes de primera calidad", precio=29990 , porcDesctoSubscriptor= 0, porcDesctoOferta=0, imagen="images/alimentoP4.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="5", nomProducto='Ruffwear Knot A Collar Red', descripcion="Correa sencilla, reflectiva, ajustable para perros", precio=20990 , porcDesctoSubscriptor= 0, porcDesctoOferta=0, imagen="images/accesorioP1.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="6", nomProducto='Eco Moon Cushion - Blue', descripcion="Cama suave para perros 100% ecológica", precio=33990 , porcDesctoSubscriptor= 0, porcDesctoOferta=0, imagen="images/accesorioP2.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="7", nomProducto='Oleron Colchon Oval Azul', descripcion="Oleron Colchon acolchonado y cómodo", precio=12990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/accesorioP3.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="8", nomProducto='Front Range - Harness', descripcion="Arnés acolchonado y cómodo", precio=38990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/accesorioP4.jpg", cantidad=1  , categoria=Categoria.objects.get(idCategoria=1))
        Producto.objects.create(idProducto="9", nomProducto='Wellness Core Cat Ocean', descripcion="Alimento completo para gatos con salmón del océano y atún", precio=42990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/alimentoG1.png", cantidad=1  , categoria=Categoria.objects.get(idCategoria=2))
        Producto.objects.create(idProducto="10", nomProducto='Fit Formula Gato Adulto', descripcion="Alimento premium para gatos adultos de 1 a 7 años", precio=24990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/alimentoG2.png", cantidad=1  , categoria=Categoria.objects.get(idCategoria=2))
        Producto.objects.create(idProducto="11", nomProducto='Wellness Core Cat Original Sterilised Salmon', descripcion="Alimento completo para gatos adultos esterilizados con salmón", precio=42990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/alimentoG3.png", cantidad=1  , categoria=Categoria.objects.get(idCategoria=2))
        Producto.objects.create(idProducto="12", nomProducto='Proplan Kitten Optistart', descripcion="Alimento súper premium para gatos cachorros(gatitos)", precio=28990 , porcDesctoSubscriptor=0 , porcDesctoOferta=0, imagen="images/alimentoG4.png", cantidad=1  , categoria=Categoria.objects.get(idCategoria=2))
        print("Tabla Producto fue poblada.")
    except Exception as err:
        print(f"Error al poblar productos: {err}")
    return redirect(home)