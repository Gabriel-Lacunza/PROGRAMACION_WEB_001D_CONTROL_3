from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from django.contrib.auth.models import User

urlpatterns = [
    path('', home, name="home"),
    path('producto_ficha_anon/<id>', producto_ficha, name="producto_ficha"),
    path('sobre_nosotros', sobre_nosotros, name="sobre_nosotros"),
    path('registrar/', registrar_usuario, name="registrar_usuario"),
    path('maestro_producto/<action>/<id>', maestro_producto, name="maestro_producto"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('mainAdministrador', mainAdministrador , name="mainAdministrador"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('maestro_bodega/<action>/<id>', maestro_bodega, name="maestro_bodega"),
    path('inicio_cliente', inicio_cliente, name='inicio_cliente'),
    path('mis_datos/<id>', mis_datos, name="mis_datos"),
    path('maestro_usuario/<action>/<id>', maestro_usuario, name="maestro_usuario"),
    path('mi_perfil', mi_perfil, name="mi_perfil"),
    path('compra_exitosa/<action>/<id>', compra_exitosa, name="compra_exitosa"),
    path('carrito', carrito, name="carrito"),
    path('mis_compras', mis_compras, name="mis_compras"),
    path('detalle_factura', detalle_factura, name="detalle_factura"),
]