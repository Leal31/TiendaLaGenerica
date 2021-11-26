from django.shortcuts import render
import requests

# Create your views here.

def reportes(request):

    return render(request, "reportes/reportes.html")
def listadoclientes(request):
    response = requests.get('http://localhost:8002/api/clientes/')
    data= response.json()
    print(response.json())
    return render(request, "reportes/listadoclientes.html", {"data": data})
def ventaclientes(request):
    response = requests.get('http://localhost:8002/api/ventas/')
    data= response.json()
    print(response.json())
    return render(request, "reportes/listadoclientes.html")