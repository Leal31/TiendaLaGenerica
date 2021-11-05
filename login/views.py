from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Usuario
from django.core.exceptions import *
# Create your views here.
def main(request):
    autenticar = True
    return render(request, 'login/index.html', {'autenticar' : autenticar})


def Autenticar(request):
        if request.method == 'POST':
            usuario = request.POST.get("usuario")
            contraseña = request.POST.get("password")
            str(contraseña)
            autenticar = Usuario.objects.filter(Usuario=usuario, Contraseña=contraseña).exists()
            if autenticar:
                return HttpResponseRedirect('tienda')
            else:
                autenticar = False
                return render(request, 'login/index.html', {'autenticar' : autenticar})
