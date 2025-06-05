from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

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
def personaCreateView(request):
    print('GET: ', request.GET)
    print('POST: ', request.POST)
    context = {}
    return render(request, 'personas/personasCreate.html', context)
def searchForHelp(request):
    return render(request, 'personas/search.html')