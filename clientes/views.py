from django.shortcuts import render
import requests

# Create your views here.
def tienda(request):
    data=None
    mensaje = None
    return render(request,'clientes/cliente.html',{"data":data, 'mensaje':mensaje})

def consultar(request):
    cedula = int(request.POST.get("cedula_cliente"))
    response= requests.get(f'http://localhost:8002/api/clientes/{cedula}/')
    data=response.json()
    mensaje = None
    return render(request, "clientes/cliente.html", {"data":data, 'mensaje' : mensaje})

def crear(request):
    nombre = request.POST.get('nombre_cliente')
    cedula = request.POST.get('cedula_cliente')
    telefono = request.POST.get('telefono_cliente')
    email= request.POST.get('email_cliente')
    direccion =request.POST.get('direccion_cliente')
    dato={"cedula": cedula,"nombre": nombre, "telefono":telefono, "email":email,"direccion":direccion}
    response =requests.post("http://localhost:8002/api/clientes/",data=dato)
    data=None
    mensaje = "El cliente fue agregado correctamente"
    return render(request, "clientes/cliente.html", {"data":data, 'mensaje' : mensaje})

def actualizar(request):
    nombre = request.POST.get('nombre_cliente')
    cedula = request.POST.get('cedula_cliente')
    telefono = request.POST.get('telefono_cliente')
    email= request.POST.get('email_cliente')
    direccion =request.POST.get('direccion_cliente')
    dato={"cedula": cedula,"nombre": nombre, "telefono":telefono, "email":email,"direccion":direccion}
    response=requests.put(f'http://localhost:8002/api/clientes/{cedula}/',data=dato)
    data=None
    mensaje = "El cliente fue actualizado satisfactoriamente"
    return render(request, "clientes/cliente.html", {"data":data, 'mensaje' : mensaje})

def borrar(request):
    cedula = int(request.POST.get("cedula_cliente"))
    response= requests.delete(f'http://localhost:8002/api/clientes/{cedula}/')
    data=None
    mensaje = "El cliente fue eliminado satisfactoriamente"
    return render(request, "clientes/cliente.html", {"data":data, 'mensaje' : mensaje})
