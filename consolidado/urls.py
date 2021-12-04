from django.urls import path
from . import views

urlpatterns = [
    path('', views.consolidado, name = 'consolidado'),
    path('calcularConsolidado/', views.calcularConsolidado, name = 'calcularCons')
]
