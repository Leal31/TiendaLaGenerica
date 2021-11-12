from django.urls import path
from . import views
urlpatterns = [
    path('', views.proveedores, name = 'proveedores'),
    path('consultar/', views.consultar, name = 'consultar_pro'),
    path('crear/', views.crear, name = 'crear_pro'),
    path('actualizar/', views.actualizar, name = 'actualizar_pro'),
    path('borrar/', views.borrar, name = 'borrar_pro')
]
