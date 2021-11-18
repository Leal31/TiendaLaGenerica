from django.urls import path
from . import views
urlpatterns = [
    path('', views.ventas, name = 'ventas'),
    path('consultarCliente/', views.consultarCliente, name = 'consultarCliente'),
    path('consultarProductos/', views.consultarProductos, name = 'consultarProductos'),
]
