from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
from django.views.generic.list import (ListView,)
from django.views.generic.detail import (DetailView,)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse

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
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    #print('GET: ', request.GET)
    #print('POST: ', request.POST)
    context = {}
    return render(request, 'personas/personasCreate.html', context)
def searchForHelp(request):
    return render(request, 'personas/search.html')
class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte= '40')
class PersonaDetailView(DetailView):
    model = Persona
class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'email',
        'activo'
    ]
class PersonaUpdateView(UpdateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'email',
        'activo'
    ]
class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')
class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hola mundo con clases')