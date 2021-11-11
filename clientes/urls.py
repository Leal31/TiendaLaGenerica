from django.urls import path, include
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.tienda, name= 'clientes'),
    path('consultar/',views.consultar, name = 'consultar'),
    path('crear/', views.crear, name = 'crear'),


]
