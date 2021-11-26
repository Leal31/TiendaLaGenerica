from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportes, name = 'reportes'),
    path('listadoclientes', views.listadoclientes, name = 'listadoclientes'),
    path('ventaclientes', views.ventaclientes, name='ventaclientes'),
]