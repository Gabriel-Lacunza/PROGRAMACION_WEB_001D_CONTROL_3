from distutils import core
from rest_framework import serializers
from core.models import *
from rest_framework.parsers import JSONParser,ParseError

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = ['idProducto','nomProducto','descripcion','precio','porcDesctoSubscriptor','porcDesctoOferta','imagen','cantidad','categoria'] 