from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos, name = 'productos'),
    path('/leercsv', views.cargar, name='leer'),
    path('/importar', views.importar, name='importar'),
]
