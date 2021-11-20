from django.urls import path
from . import views
urlpatterns = [
    path('', views.ventas, name = 'ventas'),
    path('consultas/', views.consultarTodo, name = 'consultarTodo'),
    path('subirVenta', views.subirVenta, name = 'subirVenta'),
]
