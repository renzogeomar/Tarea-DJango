from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_inicio(*args, **kwargs):
    return HttpResponse('<h1>Bienvenido a la lista de contactos</h1>')