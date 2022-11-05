from django.shortcuts import render
from django.http import HttpResponse
from .models import Cafe, Cafetera, Herramienta

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