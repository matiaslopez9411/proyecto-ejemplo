from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {"nombre": nombre} #si ponemos en el URL la variable <nombre> podemos agregar request por url
    )

def buscar(request): #nos permite agregar un request por un query (búsqueda)
    lista_de_nombres = ["Germán", "Daniel", "Romero", "Álvaro"]
    query = request.GET['q'] #para ver que contiene la request de get. GET es un diccionario, 'q' tiene la consulta
    #GET: para analizar la request y que tiene el "q". En URL se pone ?q="string" para llamar al query

    if query in lista_de_nombres: #Con el IF busco si está el nombre o no
        indice_de_resultado = lista_de_nombres.index(query)
        resultado = lista_de_nombres[indice_de_resultado] #Recordar poner [] si quiero indexar en un dict
        
    else:
        resultado = 'no hay match'

    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})