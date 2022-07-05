from rest_framework import serializers
from main.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['imagenProducto', 'idProduco', 'categoria', 'nombreProducto', 'precioProducto', 'descripcionProducto', 'disponibilidadProducto', 'porcentageSuscripcion', 'procentageOferta']