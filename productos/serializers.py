from rest_framework import serializers
from .models import Productos

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['codigo_producto', 'nombre_producto', 'nitproveedor', 'precio_compra', 'ivacompra', 'precio_venta']

