from django.urls import path
from buscaminas1 import views

urlpatterns = [
    path('', views.crea_tablero, name='nombre_de_la_vista'),
    path('crea_tablero/', views.crea_tablero, name='crea_tablero'),
]
