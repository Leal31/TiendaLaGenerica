from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import *
import csv

# Create your views here.
def productos(request):
    
    return render(request, 'productos/Productos.html')

def cargar(request):

    return render(request, 'productos/Productos.html')

def importar(request):

    nombre_archivo=("C:/Users/bryanes/Desktop/TiendaLaGenerica/productos/Productos.csv")

    with open(nombre_archivo, "r") as archivo:
    
        for linea in archivo:
            linea=linea.rstrip()
            separador=","
            lista=linea.split(",")
            productos=Productos(
                codigo_producto=int(lista[0]),
                nombre_producto=lista[1],
                nitproveedor=int(lista[2]),
                precio_compra=float(lista[3]),
                ivacompra=float(lista[4]),
                precio_venta=float(lista[5])
            )
            Productos.save(productos)


    return render(request, 'productos/Productos.html')

