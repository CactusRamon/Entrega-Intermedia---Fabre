from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cafe, Cafetera, Herramienta
from .forms import CafeFormulario, CafeteraFormulario, HerramientaFormulario

# Create your views here.

def cafe(request, nombre, origen, tueste):
    cafe = Cafe(nombre=nombre, origen=origen, tueste=tueste)
    cafe.save()
    return HttpResponse(f"""
        <p>Nombre: {cafe.nombre} - Origen: {cafe.origen} - {cafe.tueste} agregado! </p>
    """)

def lista_cafe(request):
    lista = Cafe.objects.all()
    return render(request, "lista_cafes.html", {"lista_cafes": lista})

def cafetera(request, metodo, nombre):
    cafetera = Cafetera(metodo=metodo, nombre=nombre)
    cafetera.save()
    return HttpResponse(f"""
        <p>Metodo: {cafetera.metodo} - Nombre: {cafetera.nombre} agregado! </p>
    """)

def lista_cafetera(request):
    lista = Cafetera.objects.all()
    return render(request, "lista_cafeteras.html", {"lista_cafeteras": lista})

def herramienta(request, metodo, material):
    herramienta = Herramienta(metodo=metodo, material=material)
    herramienta.save
    return HttpResponse((f"""
        <p>Nombre: {herramienta.nombre} agregado! </p>
    """))

def lista_herramienta(request):
    lista = Herramienta.objects.all()
    return render(request, "lista_herramientas.html", {"lista_herramientas": lista})

def home(request):
     return render(request, "home.html")

def cafes(request):
     lista = Cafe.objects.all()
     return render(request, "cafes.html", {"lista_cafes": lista})

def cafeteras(request):
     lista = Cafetera.objects.all()
     return render(request, "cafeteras.html", {"lista_cafeteras": lista})

def herramientas(request):
     lista = Herramienta.objects.all()
     return render(request, "herramientas.html", {"lista_herramientas": lista})

def cafeFormulario(request):
    print("method: ", request.method)
    print("post: ", request.POST)

    if request.method == 'POST':
        mi_formulario = CafeFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            cafe = Cafe(nombre=data['nombre'], origen=data['origen'], tueste=data['tueste'])
            cafe.save()
            return redirect('Cafes')
    else:
        mi_formulario= CafeFormulario()
    return render(request, "cafeFormulario.html", {"mi_formulario": mi_formulario})

def cafeteraFormulario(request):
    print("method: ", request.method)
    print("post: ", request.POST)

    if request.method == 'POST':
        mi_formulario = CafeteraFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            cafetera = Cafetera(metodo=data['metodo'], nombre=data['nombre'])
            cafetera.save()
            return redirect('Cafeteras')
    else:
        mi_formulario= CafeteraFormulario()
    return render(request, "cafeteraFormulario.html", {"mi_formulario": mi_formulario})

def herramientaFormulario(request):
    print("method: ", request.method)
    print("post: ", request.POST)

    if request.method == 'POST':
        mi_formulario = HerramientaFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            herramienta = Herramienta(nombre=data['nombre'])
            herramienta.save()
            return redirect('Cafes')
    else:
        mi_formulario= HerramientaFormulario()
    return render(request, "herramientaFormulario.html", {"mi_formulario": mi_formulario})

def busqueda_cafe(request):
    return render(request, "busqueda_cafe.html")

def busqueda_cafetera(request):
    return render(request, "busqueda_cafetera.html")

def busqueda_herramienta(request):
    return render(request, "busqueda_herramienta.html")   

def buscar(request):

    cafe_buscado=request.GET["nombre"]
    cafe = Cafe.objects.get(nombre = cafe_buscado)
    return render (request, "resultadoBusqueda.html", {"cafe": cafe})

    #cafetera_buscada=request.GET["cafetera"]
    #herramienta_buscada=request.GET["herramienta"]