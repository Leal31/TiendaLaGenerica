from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from pathlib import Path
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.http import Http404

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
            if extension == '.csv':
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
            elif extension != '.csv' and extension != '':
                mensaje = "El archivo no tiene una extension valida"
                return render(request, 'productos/Productos.html', {'mensaje' : mensaje})
            else:
                raise IsADirectoryError()
    except IsADirectoryError:
        mensaje = "El archivo no ha sido cargado"
        return render(request, 'productos/Productos.html', {'mensaje' : mensaje})


class Producto_CRUD(APIView):

    def get(self, request, format=None, *args, **kwars):
        productos = Productos.objects.all()
        serializer = ProductoSerializers(productos, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Producto_Vista(APIView):
    def obtener_producto(self, pk):
        try:
            return Productos.objects.get(codigo_producto = pk)
        except Productos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto =  self.obtener_producto(pk)
        serializer = ProductoSerializers(producto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        producto = self.obtener_producto(pk)
        serializer = ProductoSerializers(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.obtener_cliente(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




