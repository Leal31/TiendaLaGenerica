from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from pathlib import Path
import os
import requests

# Create your views here.
def productos(request):
    mensaje = None
    return render(request, 'productos/Productos.html', {'mensaje' : mensaje})

def cargar(request):

    if request.method == 'POST':
        BASE_DIR = Path(__file__).resolve().parent.parent
        direccion = f"{BASE_DIR}/productos/static/{request.POST.get('fileupload')}"
        root, extension = os.path.splitext(direccion)
        if extension == '.csv':
            mensaje = "El archivo es valido"
            return render(request, 'productos/Productos.html', {'mensaje' :  mensaje})
        elif extension != '' and extension != '.csv':
            mensaje = "El archivo no es valido"
            return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
        elif extension == '':
            mensaje = "No ha sido cargado ningun archivo"
            return render(request, 'productos/Productos.html', {'mensaje' : mensaje})



def importar(request):
    try:
        if request.method == 'POST':
            BASE_DIR = Path(__file__).resolve().parent.parent
            direccion = f"{BASE_DIR}/productos/static/{request.POST.get('fileupload')}"
            root, extension = os.path.splitext(direccion)
            listapro = []
            if extension == '.csv':
                with open(direccion, "r") as archivo:

                    for linea in archivo:
                        linea=linea.rstrip()
                        separador=","
                        lista=linea.split(",")
                        productos = {
                            'codigo_producto' : int(lista[0]),
                            'nombre_producto' : lista[1],
                            'nitproveedor' : int(lista[2]),
                            'precio_compra' : float(lista[3]),
                            'ivacompra' : float(lista[4]),
                            'precio_venta' : float(lista[5])
                        }
                        listapro.append(productos)
                        mensaje = "El archivo fue subido con exito"
                return render(request, 'productos/Productos.html', {'mensaje' : mensaje, 'csv' : listapro})
            elif extension != '.csv' and extension != '':
                mensaje = "El archivo no tiene una extension valida"
                return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
            else:
                raise IsADirectoryError()
    except IsADirectoryError:
        mensaje = "El archivo no ha sido cargado"
        return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
