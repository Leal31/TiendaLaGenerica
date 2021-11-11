from django.shortcuts import render
import requests

# Create your views here.
def tienda(request):
    data=None
    return render(request,'cliente.html',{"data":data})

def consultar(request):
    cedula = int(request.POST.get("cedula_cliente"))
    response= requests.get(f'http://localhost:8000/api/clientes/{cedula}/')
    data=response.json()
    return render(request, "cliente.html", {"data":data})

def crear(request):
    nombre = request.POST.get('nombre_cliente')
    cedula = request.POST.get('cedula_cliente')
    telefono = request.POST.get('telefono_cliente')
    email= request.POST.get('email_cliente')
    direccion =request.POST.get('direccion_cliente')
    dato={"cedula": cedula,"nombre": nombre, "telefono":telefono, "email":email,"direccion":direccion}
    response =requests.post("http://localhost:8000/api/clientes/",data=dato)
    data=None
    return render(request, "cliente.html", {"data":data})
