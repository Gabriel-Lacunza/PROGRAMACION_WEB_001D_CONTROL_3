from distutils import core
from rest_framework import serializers
from core.models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = '__all__' 