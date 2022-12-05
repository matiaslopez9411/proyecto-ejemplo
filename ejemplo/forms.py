from django import forms #No es necesario generar un uevo .py, puede ir en views.py pero no es recomendado!

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100) #Se pueden tener diferentes tipos de campos (datos) en el formulario
#Se define el tipo de dato pq cuando el template renderiza el formulario, Django inserta ciertas funcionalidades gráficas que validan los datos.

