from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Usuario
from django.core.exceptions import *
from principal.views import tienda
# Create your views here.
def main(request):
    return render(request, 'login/index.html')


def Autenticar(request):
    try:

        usuario = request.POST.get("usuario")
        contraseña = request.POST.get("password")
        str(contraseña)
        autenticar = Usuario.objects.filter(Usuario=usuario, Contraseña=contraseña).exists()
        if autenticar:
            autenticado = Usuario.objects.get(Usuario=usuario, Contraseña=contraseña)
            return HttpResponseRedirect('tienda')
        else:
            return HttpResponseRedirect('/')

    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
