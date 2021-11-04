from django.shortcuts import render
from login.models import Usuario
# Create your views here.
def tienda(request):

    return render(request, 'principal/principal.html')
