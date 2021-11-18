from django.shortcuts import render, redirect
import requests
# Create your views here.
def ventas(request):
    data = None
    Mensaje = None
    return render(request, 'ventas/ventas.html', {'Cliente' : data})

def consultarCliente(request):
    try:
        cedula = request.POST.get('cedula_cliente')
    except Exception:
        print('hubo un error')
    int(cedula)
    response = requests.get(f'http://localhost:8002/api/clientes/{cedula}/')

    if response.status_code == 200:

        data = response.json()
        mensaje = None
    elif response.status_code == 404:
        data = None
        mensaje = "No se encontro el cliente"

    return render(request, 'ventas/ventas.html', {'Cliente' : data})

def consultarProductos(request):
    try:
        producto1 = request.POST.get('codigo_producto')
        producto2 = request.POST.get('codigo_producto2')
        producto3 = request.POST.get('codigo_producto3')
    except Exception:
        print('algo ha salido mal')
    if (producto1 == '' and producto2 == '') and producto3 == '':
        data1 = None
        data2 = None
        data3 = None
        mensaje = "No hay ningun producto ingresado"
        condicional = "todovacio"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
    elif producto1 == '' and producto2 == '':
        mensaje = None
        condicional = "lleno3"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
    elif producto2 == '' and producto3 == '':
        mensaje = None
        condicional = "lleno1"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
    elif producto1 == '' and producto3 == '':
        mensaje = None
        condicional = "lleno2"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
    elif producto1 == '':
        mensaje = None
        condicional = "vacio1"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
    elif producto2 == '':
        mensaje = None
        condicional = "vacio2"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
    elif producto3 == '':
        mensaje = None
        condicional = "vacio3"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional})
