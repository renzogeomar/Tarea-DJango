from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    contex = {
        'objeto' : obj,
    }
    return render(request, 'personas/test.html', contex)
def descripcion(request):
    obj = Persona.objects.get(id=1)
    contex = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html',contex)
