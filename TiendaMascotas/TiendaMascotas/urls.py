"""
TiendaMascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carritoCompra/', carrito_de_compras, name='carritoCompra'),
    path('detalleFactura/', detalle_factura, name='detalleFactura'),
    path('fichaProducto/<int:idProduco>/', ficha_producto, name='fichaProducto'),
    path('historialVentas/', historial_de_ventas, name='historialVentas'),
    path('ingresar/', ingresar, name='ingresar'),
    path('inicioAdministrador/', inicio_como_administrador, name='inicioAdministrador'),
    path('inicioCli/', inicio_como_cliente, name='inicioCli'),
    path('', inicio_usuario_anonimo, name='inicioAnonimo'),
    path('mantenedorBodega/', mantenedor_de_bodega, name='mantenedorBodega'),
    path('mantenedorProducto/<idProducto>/<action>', mantenedor_de_productos, name='mantenedorProducto'),
    path('mantenedorUsuario/<idUsuario>/<action>', mantenedor_de_usuario, name='mantenedorUsuario'),
    path('menuAdmin/', menu_de_administracion, name='menuAdmin'),
    path('misCompras/', mis_compras, name='misCompras'),
    path('nosotros/', nosotros, name='nosotros'),
    path('registrarse/', registrarse, name='registrarse'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
