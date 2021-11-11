from django.shortcuts import render
import requests 

# Create your views here.
def tienda(request):
    data=None
    return render(request,'cliente.html',{"data":data})
def consultar(request,cedula):
    cedula = request.POST.get("cedula_cliente")
    response= requests.get('localhost:8000/api/clientes/',cedula)
    data=response.json()
    return render (request, "cliente.html", {"data":data})