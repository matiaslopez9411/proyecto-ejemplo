from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar
from django.views import View

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
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares}) #este contexto va al html, seria la lista que lee con el for

#FORM:
#Vamos a tener que definir una views que genere un GET y un POST
#GET: permite renderizar la interfáz gráfica
#POST: busca el "familiar" y lo muestra.
class Buscarfamiliar(View): #clase View definida por Django, la nueva clase va a heredar sus atributos
    form_class = Buscar #Poner el form que se va a usar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() #Hasta acá definimos la consulta, con el .all decimos cuantas consultas hace python
            return render(request, self.template_name, 
            {'form':form, 'lista_familiares': lista_familiares})

        
        return render(request, self.template_name, {'form': form})