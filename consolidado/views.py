from django.http import response
from django.shortcuts import render
import requests

def consolidado(request):
    responseget = requests.get("http://localhost:8005/api/consolidado/")
    listaventa = []
    if responseget.status_code == 200:
        datacon = responseget.json()
        for i in datacon:
            listaventa.append(i['total_ventas'])
        suma = sum(listaventa)
    else:
        datacon = None

    return render(request, "consolidado/Consolidacion.html", {'consolidados' : datacon, 'total' : suma})

def calcularConsolidado(request):
    responseget = requests.get("http://localhost:8005/api/consolidado/1/")
    responseventa = requests.get("http://localhost:8004/api/ventas/")
    data = responseventa.json()
    listaventas = []
    for i in data:
        listaventas.append(i['valor_venta'])

    sumaventas = sum(listaventas)
    datacon = {'ciudad' : 'Bogota', 'total_ventas' : sumaventas }
    if responseget.status_code == 200:
        responseput = requests.put("http://localhost:8005/api/consolidado/1/", data=datacon)
        responseget = requests.get("http://localhost:8005/api/consolidado/")
        dataconsolidado = responseget.json()
    elif responseget.status_code == 404:
        responsepost = requests.post("http://localhost:8005/api/consolidado/", data=datacon)
        responseget = requests.get("http://localhost:8005/api/consolidado/")
        dataconsolidado = responseget.json()

    return render(request, "consolidado/Consolidacion.html", {'consolidados' : dataconsolidado, 'total' : sumaventas})
        



    
