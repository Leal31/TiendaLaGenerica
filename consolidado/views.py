from django.http import response
from django.shortcuts import render
import requests

def consolidado(request):
    responseventa= requests.get('http://localhost:8004/api/ventas/')
    sumaventa= []
    if responseventa.status_code==200:
       data= responseventa.json()
    for i in data:
        sumaventa.append(i['total_venta'])
    totalventa= sum(sumaventa)
    dataconsolidado= {'ciudad':'bogota','total_ventas':totalventa}
    responseconsolidado= requests.post('http://localhost:8005/api/consolidado/', data=dataconsolidado)
    if responseconsolidado.status_code == 201:
        responseget = requests.get("http://localhost:8005/api/consolidado/")
        datacon = responseget.json()

    return render(request, "consolidado/Consolidacion.html", {'consolidados' : datacon})
