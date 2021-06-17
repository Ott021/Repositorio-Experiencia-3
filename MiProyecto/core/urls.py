from django.urls import path
from django.urls import URLPattern
from .views import index, contacto, listarVehiculos,agregarVehiculo

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('vehiculo/listar',listarVehiculos, name="listarVehiculos"),
    path('vehiculo/agregar',agregarVehiculo,name="agregarVehiculo")
]