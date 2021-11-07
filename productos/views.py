from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import *
import csv
from pathlib import Path
# Create your views here.
def productos(request):
    mensaje = False
    return render(request, 'productos/Productos.html', {'mensaje' : mensaje})

def cargar(request):

    return render(request, 'productos/Productos.html')

def importar(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    direccion = f"{BASE_DIR}\productos\static\{request.POST.get('fileupload')}"
    with open(direccion, "r") as archivo:

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
            mensaje = True
    return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
