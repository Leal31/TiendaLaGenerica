from django.urls import path
from . import views

urlpatterns = [
    path('', views.consolidado, name = 'consolidado'),
]