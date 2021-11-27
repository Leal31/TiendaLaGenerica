from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportes, name = 'reportes'),
    path('listadoclientes/', views.listadoclientes, name = 'listadoclientes'),
    path('ventaclientes/<int:cedula>', views.ventaclientes, name='ventaclientes'),
]
