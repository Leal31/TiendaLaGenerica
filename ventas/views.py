from django.shortcuts import render, redirect
import requests
# Create your views here.
def ventas(request):
    data = None
    Mensaje = None
    return render(request, 'ventas/ventas.html', {'Cliente' : data})


def consultarTodo(request):
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


    try:
        producto1 = request.POST.get('codigo_producto')
        producto2 = request.POST.get('codigo_producto2')
        producto3 = request.POST.get('codigo_producto3')
        cantidad1 = request.POST.get('cantidad1')
        cantidad2 = request.POST.get('cantidad2')
        cantidad3 = request.POST.get('cantidad3')
    except Exception:
        print('algo ha salido mal')

    if (producto1 == '' and producto2 == '') and producto3 == '':
        data1 = None
        data2 = None
        data3 = None
        mensaje = "No hay ningun producto ingresado"
        condicional = "todovacio"
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'condicional' : condicional, 'Cliente':data})
    elif producto1 == '' and producto2 == '':
        mensaje = None
        condicional = "lleno3"
        response= requests.get(f"http://localhost:8001/api/productos/{producto3}/")
        data1=None
        data2=None
        data3= response.json()
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional, 'cantidad3' : cantidad3, 'Cliente' : data})
    elif producto2 == '' and producto3 == '':
        mensaje = None
        condicional = "lleno1"
        response= requests.get(f"http://localhost:8001/api/productos/{producto1}/")
        data1=response.json()
        data2=None
        data3=None
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional, 'cantidad1' : cantidad1, 'Cliente': data})
    elif producto1 == '' and producto3 == '':
        mensaje = None
        condicional = "lleno2"
        response= requests.get(f"http://localhost:8001/api/productos/{producto2}/")
        data1=None
        data2= response.json()
        data3=None
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional, 'cantidad2': cantidad2, 'Cliente':data})
    elif producto1 == '':
        mensaje = None
        condicional = "vacio1"
        response= requests.get(f"http://localhost:8001/api/productos/{producto2}/")
        response1= requests.get(f"http://localhost:8001/api/productos/{producto3}/")
        data1=None
        data2=response.json()
        data3=response1.json()
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional,'cantidad2': cantidad2,'cantidad3': cantidad3, 'Cliente' : data})
    elif producto2 == '':
        mensaje = None
        condicional = "vacio2"
        response= requests.get(f"http://localhost:8001/api/productos/{producto1}/")
        response1= requests.get(f"http://localhost:8001/api/productos/{producto3}/")
        data1=response.json()
        data2=None
        data3=response1.json()
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional,'cantidad1': cantidad1,'cantidad3': cantidad3, 'Cliente' : data})
    elif producto3 == '':
        mensaje = None
        condicional = "vacio3"
        response= requests.get(f"http://localhost:8001/api/productos/{producto1}/")
        response1= requests.get(f"http://localhost:8001/api/productos/{producto2}/")
        data1=response.json()
        data2=response1.json()
        data3=None
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional,'cantidad1': cantidad1,'cantidad2': cantidad2, 'Cliente' : data})
    elif (producto1 != None and producto2!=None)and producto3!=None:
        mensaje = None
        condicional ="todosllenos"
        response= requests.get(f"http://localhost:8001/api/productos/{producto1}/")
        response1= requests.get(f"http://localhost:8001/api/productos/{producto2}/")
        response2= requests.get(f"http://localhost:8001/api/productos/{producto3}/")
        data1=response.json()
        data2=response1.json()
        data3=response2.json()
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional, 'cantidad1' : cantidad1, 'cantidad2' : cantidad2, 'cantidad3' : cantidad3, 'Cliente' : data})
    else:
        mensaje= None
        condicional = None
        data1=None
        data2=None
        data3=None
        return render(request, 'ventas/ventas.html', {'mensaje' : mensaje, 'data1' : data1, 'data2' : data2, 'data3': data3, 'condicional' : condicional, 'Cliente': data})

def subirVenta(request):
    cedula_cliente=request.POST.get('cedula_cliente')
    nombre_cliente=request.POST.get('nombre_cliente')
    consecutivo=request.POST.get('consec')
    codigo_producto1=request.POST.get('codigo_producto')
    codigo_producto2=request.POST.get('codigo_producto2')
    codigo_producto3=request.POST.get('codigo_producto3')
    nombre_producto1=request.POST.get('nombre_producto')
    nombre_producto2=request.POST.get('nombre_producto2')
    nombre_producto3=request.POST.get('nombre_producto3')
    cantidad1=request.POST.get('cantidad1')
    cantidad2=request.POST.get('cantidad2')
    cantidad3=request.POST.get('cantidad3')
    precio1=request.POST.get('total_venta1')
    precio2=request.POST.get('total_venta2')
    precio3=request.POST.get('total_venta3')
    total_compra=request.POST.get('total_venta')
    iva_venta=request.POST.get('ivaventa')
    total_venta=request.POST.get('valor_venta')

    data3productos = {
    "cedula_cliente": cedula_cliente,
    "codigo_venta": consecutivo,
    "detalle_venta": [{
                    "cantidad_producto": cantidad1,
                    "codigo_producto": codigo_producto1, 
                    "valor_total": precio1,
                    "valor_venta": precio1,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad2,
                    "codigo_producto": codigo_producto2,
                    "valor_total": precio2,
                    "valor_venta": precio2,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad3,
                    "codigo_producto": codigo_producto3,
                    "valor_total": precio3,
                    "valor_venta": precio3,
                    "valoriva": 19.0
                    }],
    "iva_venta": iva_venta,
    "total_venta": total_compra,
    "valor_venta": total_venta
}             
                
            

    if codigo_producto1 == '':
        data2productos = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [
                    {
                    "cantidad_producto": cantidad2,
                    "codigo_producto": codigo_producto2,
                    "valor_total": precio2,
                    "valor_venta": precio2,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad3,
                    "codigo_producto": codigo_producto3,
                    "valor_total": precio3,
                    "valor_venta": precio3,
                    "valoriva": 19.0
                    }],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }  

        response = requests.post('http://localhost:8004/api/ventas/', json=data2productos)

        exito = True
    elif codigo_producto2 == '':
        data2productos = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [
                    {
                    "cantidad_producto": cantidad1,
                    "codigo_producto": codigo_producto1,
                    "valor_total": precio1,
                    "valor_venta": precio1,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad3,
                    "codigo_producto": codigo_producto3,
                    "valor_total": precio3,
                    "valor_venta": precio3,
                    "valoriva": 19.0
                    }],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }

        response = requests.post("http://localhost:8004/api/ventas/", json=data2productos)

        exito = True
    elif codigo_producto3 == '':
        data2productos = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [
                    {
                    "cantidad_producto": cantidad1,
                    "codigo_producto": codigo_producto1,
                    "valor_total": precio1,
                    "valor_venta": precio1,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad2,
                    "codigo_producto": codigo_producto2,
                    "valor_total": precio2,
                    "valor_venta": precio2,
                    "valoriva": 19.0
                    }],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }
        response = requests.post("http://localhost:8004/api/ventas/", json=data2productos)
        exito = True
    elif codigo_producto2 == '' and codigo_producto3 == '':
        data1producto = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [{"cantidad_producto": cantidad1, "codigo_producto": codigo_producto1, "valor_total": precio1, "valor_venta": precio1, "valoriva": 19.0}],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }

        response = requests.post("http://localhost:8004/api/ventas/", json = data1producto)
        exito = True
    elif codigo_producto1 == '' and codigo_producto3 == '':
        data1producto = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [
                    {
                    "cantidad_producto": cantidad2,
                    "codigo_producto": codigo_producto2,
                    "valor_total": precio2,
                    "valor_venta": precio2,
                    "valoriva": 19.0
                    }
                    ],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }
        response = requests.post("http://localhost:8004/api/ventas/", json=data1producto)

        exito = True
    elif codigo_producto1 == '' and codigo_producto2 == '':
        data1producto = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [
                    {
                    "cantidad_producto": cantidad3,
                    "codigo_producto": codigo_producto3,
                    "valor_total": precio3,
                    "valor_venta": precio3,
                    "valoriva": 19.0
                    }
                    ],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }
        response = requests.post("http://localhost:8004/api/ventas/", json=data1producto)

        exito = True
    elif (codigo_producto1 == '' and codigo_producto2 == '') and codigo_producto3 == '':
        exito = False
    else:
        data3productos = {
        "cedula_cliente": cedula_cliente,
        "codigo_venta": consecutivo,
        "detalle_venta": [{
                    "cantidad_producto": cantidad1,
                    "codigo_producto": codigo_producto1, 
                    "valor_total": precio1,
                    "valor_venta": precio1,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad2,
                    "codigo_producto": codigo_producto2,
                    "valor_total": precio2,
                    "valor_venta": precio2,
                    "valoriva": 19.0
                    }, {
                    "cantidad_producto": cantidad3,
                    "codigo_producto": codigo_producto3,
                    "valor_total": precio3,
                    "valor_venta": precio3,
                    "valoriva": 19.0
                    }],
        "iva_venta": iva_venta,
        "total_venta": total_compra,
        "valor_venta": total_venta
        }
        response = requests.post("http://localhost:8004/api/ventas/",json=data3productos)

        exito = True
    return render(request, 'ventas/ventas.html', {'exito' : exito})
