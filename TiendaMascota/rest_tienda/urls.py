from django.urls import path
from rest_tienda.views import *

urlpatterns = [
    path('lista_productos', lista_productos , name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto , name="detalle_producto"),
    path('producto_create', producto_create.as_view(), name="producto_create"),
    path('vehiculo_delete/<id>', vehiculo_delete, name="vehiculo_delete"),
    path('producto_update', producto_update.as_view(), name="producto_update"),
    path('login', login, name='login'),
]
