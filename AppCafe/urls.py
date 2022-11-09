from django.urls import path
from AppCafe.views import cafes, cafeteras, cafe, cafetera, lista_cafe, lista_cafetera, home, herramienta, herramientas, lista_herramienta, cafeFormulario

urlpatterns = [
    path('agrega-cafe/<nombre>/<origen>/<tueste>', cafe),
    path('agrega-cafetera/<metodo>/<nombre>', cafetera),
    path('agrega-herramientas/<nombre>', herramienta),
    path('home', home),
    path('lista-cafes/', lista_cafe),
    path('lista-cafeteras/', lista_cafetera),
    path('lista-herramientas/', lista_herramienta),
    path('cafes/', cafes, name="Cafes"),
    path('cafeteras/', cafeteras, name="Cafeteras"),
    path('herramientas/', herramientas, name="Herramientas"),
    path('cafeFormulario', cafeFormulario, name="CafeFormulario")
]