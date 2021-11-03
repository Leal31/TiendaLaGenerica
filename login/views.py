from django.shortcuts import render, HttpResponse
from .models import Usuario
# Create your views here.
def main(request):
    return render(request, 'login/index.html')


def Autenticar(request):

        usuario = request.POST.get("usuario")
        contraseña = request.POST.get("password")
        str(contraseña)
        autenticar = Usuario.objects.filter(Usuario=usuario, Contraseña=contraseña)
        if autenticar == None:
            return HttpResponse("No se encontro el usuario")
        else:
            return HttpResponse("Ingreso exitosamente al sistema")
