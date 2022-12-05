"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import index, saludar_a, buscar, mostrar_familiares, Buscarfamiliar #asigna la función ejemplo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA ruta de la NUEVA FUNCTION
    path('saludar-a/<nombre>/', saludar_a), #El <nombre> permte definir a la variable desde la URL
    path('buscar/', buscar),
    path('mi-familia/', mostrar_familiares), #vista para el modelo familiares
    path('mi-familia/buscar', Buscarfamiliar.as_view())
]
