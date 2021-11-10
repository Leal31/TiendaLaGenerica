from django.db import models

# Create your models here.
class Clientes(models.Model):
    cedula=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=255)
    direccion=models.CharField(max_length=255)
    telefono=models.CharField(max_length=255)
    email=models.EmailField(null=True)