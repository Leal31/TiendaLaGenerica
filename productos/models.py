from django.db import models

# Create your models here.

class Productos(models.Model):

    codigo_producto=models.IntegerField(primary_key=True)
    nombre_producto=models.CharField(max_length=255, null=True)
    nitproveedor=models.IntegerField()
    precio_compra=models.FloatField()
    ivacompra=models.FloatField()
    precio_venta=models.FloatField()
