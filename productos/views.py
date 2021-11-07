from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from pathlib import Path
import os
# Create your views here.
def productos(request):
    mensaje = False
    return render(request, 'productos/Productos.html', {'mensaje' : mensaje})

def cargar(request):

    return render(request, 'productos/Productos.html')

def importar(request):
    try:
        if request.method == 'POST':
            BASE_DIR = Path(__file__).resolve().parent.parent
            direccion = f"{BASE_DIR}/productos/static/{request.POST.get('fileupload')}"
            root, extension = os.path.splitext(direccion)
            if extension == 'csv' and extension != None:
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
                        mensaje = "El archivo fue subido correctamente"
                return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
            elif extension != 'csv' and extension != '':
                mensaje = "El archivo no tiene una extension valida"
                return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
            else:
                raise IsADirectoryError()
    except IsADirectoryError:
        mensaje = "El archivo no ha sido cargado"
        return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
