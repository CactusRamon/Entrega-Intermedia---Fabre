from django.urls import path
from AppCafe.views import cafes, cafeteras, cafe, cafetera, lista_cafe, lista_cafetera, home, herramienta, herramientas, lista_herramienta, cafeFormulario, cafeteraFormulario, herramientaFormulario, busqueda_cafe, busqueda_cafetera, busqueda_herramienta, buscar

urlpatterns = [
    path('agrega-cafe/<nombre>/<origen>/<tueste>', cafe),
    path('agrega-cafetera/<metodo>/<nombre>', cafetera),
    path('agrega-herramientas/<nombre>', herramienta),
    path('home/', home),
    path('lista-cafes/', lista_cafe),
    path('lista-cafeteras/', lista_cafetera),
    path('lista-herramientas/', lista_herramienta),
    path('cafes/', cafes, name="Cafes"),
    path('cafeteras/', cafeteras, name="Cafeteras"),
    path('herramientas/', herramientas, name="Herramientas"),
    path('cafeFormulario/', cafeFormulario, name="CafeFormulario"),
    path('cafeteraFormulario/', cafeteraFormulario, name="CafeteraFormulario"),
    path('herramientaFormulario/', herramientaFormulario, name="HerramientaFormulario"),
    path('busqueda_cafe/', busqueda_cafe, name="busqueda_cafe"),
    path('busqueda_cafetera/', busqueda_cafetera, name="busqueda_caftera"),
    path('busqueda_herramienta/', busqueda_herramienta, name="busqueda_herramienta"),
    path("buscar/", buscar, name="buscar"),
]