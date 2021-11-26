from django.shortcuts import render
import requests

# Create your views here.

def reportes(request):

    return render(request, "reportes/reportes.html")
def listadoclientes(request):
    response = requests.get("http://localhost:8002/clientes/")
    data= response.json()
    print(data)
    return render(request, "reportes/listadoclientes.html")