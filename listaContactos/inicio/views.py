from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_inicio(*args, **kwargs):
    return HttpResponse('<h1>Bienvenido a la lista de contactos</h1>')
def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')
def anotherView2(request):
    return HttpResponse('<h1>Esta es otra página de prueba</h1>')