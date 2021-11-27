from django.shortcuts import render
import requests

# Create your views here.

def reportes(request):

    return render(request, "reportes/reportes.html")
def listadoclientes(request):
    response = requests.get('http://localhost:8002/api/clientes/')
    data= response.json()
    return render(request, "reportes/listadoclientes.html", {"data": data})
def ventaclientes(request, cedula):
    print(cedula)
    response = requests.get(f"http://localhost:8004/api/ventaporcliente/{cedula}/")
    if response.status_code == 200:
        data = response.json()

    response1 = requests.get(f"http://localhost:8002/api/clientes/{cedula}/")
    if response1.status_code == 200:
        data2 = response1.json()
    return render(request, "reportes/ventasporcli.html", {'data' : data, 'datac' : data2})
