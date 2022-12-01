from django.db import models

# Create your models here.
class Familiar(models.Model): #los atributos se ven diferentes a una clase normal
#esto se debe a que tiene un ORM--> trata de mapear los atributos en una base de datos.
#Se definen los atributos como variables de clase y como valor el tipo de dato que vamos a usar
#Charfield --> campo de tipo caracter / IntegerField --> campo de enteros.

    nombre = models.CharField(max_length=100) #siempre poner el max_length
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
#Se definen así porque las base de datos relacionables te piden el tipo de las columnas en la tabla de base de datos.

    def __str__(self): #dundermethod: sirve para que cuando se ejecuta el print muestre los valores del return.
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"