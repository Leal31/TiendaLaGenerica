from django.urls import path, include
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.tienda, name= 'clientes'),
    path('consultar/<int:cedula>',views.consultar, name = 'consultar'),


]