from django.shortcuts import render
import requests
# Create your views here.
def proveedores(request):
    data = None
    mensaje = None
    return render(request, 'proveedores/proveedores.html', {'data' : data, 'mensaje' : mensaje})

def consultar(request):
    nit = int(request.POST.get('nit_pro'))
    response = requests.get(f'http://localhost:8003/api/proveedores/{nit}/')
    data = response.json()
    mensaje = None
    return render(request, 'proveedores/proveedores.html', {'data' : data, 'mensaje' : mensaje})

def crear(request):
    nit = int(request.POST.get('nit_pro'))
    nombre = request.POST.get('nombre_pro')
    direccion = request.POST.get('direccion_pro')
    telefono = request.POST.get('telefono_pro')
    ciudad = request.POST.get('ciudad_pro')
    dato = {'Nit' : nit, 'nombre_proveedor' : nombre, 'direccion_proveedor' : direccion, 'telefono_proveedor' : telefono, 'ciudad_proveedor' : ciudad}
    response = requests.post('http://localhost:8003/api/proveedores/', data=dato)
    data = None
    mensaje = "El proveedor fue creado satisfactoriamente"
    return render(request, 'proveedores/proveedores.html', {'data' : data, 'mensaje' : mensaje})

def actualizar(request):
    nit = int(request.POST.get('nit_pro'))
    nombre = request.POST.get('nombre_pro')
    direccion = request.POST.get('direccion_pro')
    telefono = request.POST.get('telefono_pro')
    ciudad = request.POST.get('ciudad_pro')
    dato = {'Nit' : nit, 'nombre_proveedor' : nombre, 'direccion_proveedor' : direccion, 'telefono_proveedor' : telefono, 'ciudad_proveedor' : ciudad}
    response = requests.put(f'http://localhost:8003/api/proveedores/{nit}/', data=dato)
    data = None
    mensaje = "El proveedor fue actualizado satisfactoriamente"
    return render(request, 'proveedores/proveedores.html', {'data' : data, 'mensaje' : mensaje})

def borrar(request):
    nit = int(request.POST.get('nit_pro'))
    response = requests.delete(f'http://localhost:8003/api/proveedores/{nit}/')
    data = None
    mensaje = "El proveedor fue eliminado satisfactoriamente"
    return render(request, 'proveedores/proveedores.html', {'data' : data, 'mensaje' : mensaje})
