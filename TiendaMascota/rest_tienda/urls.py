from django.urls import path
from rest_tienda.views import *

urlpatterns = [
    path('producto_read_all', producto_read_all , name="producto_read_all"),
    path('producto_create/', producto_create.as_view(), name="producto_create"),
    path('login', login, name='login'),
]
