from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def pagina_inicio(request, *args, **kwargs):
    myContext = {
        'myText' : 'Esto es sobre nosotros',
        'myNumber' : 123,
        'myList' : [11, 22, 33, 55, 66],
        'reversedList' : ['primero', 'segundo', 'tercero'],
        'points' : [(1,2), (3,4), (5,6)],
        'data' : {
            'nombre' : 'Renzo',
            'edad' : 18,
            'ciudad' : 'Arequipa',
        },
        'listaAtletas': ['Juan', 'Luis', 'Carlos'],
        'listaEntrenadores': ['Rodrigo'],  
        'listaCasilleros': [],
        'variable': 10,
        'saludos': ['hello', 'hi', 'hey'],
        'status': True,
        'maybe_none': None,
        'messages': ['Hola', 'Bienvenido', 'Revisa tu correo'],
        'name': 'Juan',
        'name2' : 'Carlos',
        'nickname': '',  
        'today': date.today(),
    }
    print("Args:", args)
    print("Kwargs:", kwargs)
    print("Usuario:", request.user)
    return render(request, "inicio/home.html", myContext)
def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')
def anotherView2(request):
    return HttpResponse('<h1>Esta es otra página de prueba</h1>')