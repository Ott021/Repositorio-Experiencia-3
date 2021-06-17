from core.forms import VehiculoForm
from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoForm #caso alternativo de que el por defecto este mal hecho

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def listarVehiculos(request):
    vehiculos = Vehiculo.objects.all()

    datos = {
        'vehiculos' : vehiculos
    }
    return render(request, 'core/listarVehiculos.html',datos)

def agregarVehiculo(request):

    form = VehiculoForm()

    datos = {
        'form' : VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Vehiculo agregado exitosamente'


    return render(request, 'core/agregarVehiculo.html',datos)

