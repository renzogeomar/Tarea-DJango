from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_inicio(request, *args, **kwargs):
    myContext = {
        'myText' : 'Esto es sobre nosotros',
        'myNumber' : 123,
        'myList' : [11, 22, 33, 44, 55],
    }
    print("Args:", args)
    print("Kwargs:", kwargs)
    print("Usuario:", request.user)
    return render(request, "inicio/home.html", myContext)
def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')
def anotherView2(request):
    return HttpResponse('<h1>Esta es otra página de prueba</h1>')