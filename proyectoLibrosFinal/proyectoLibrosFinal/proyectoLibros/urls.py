"""proyectoLibros URL Configuration

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
from django.urls import path, include

from appLibros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('autores/',views.listadoAutor),
    path('agregarAutor/',views.agregarAutor),
    path('eliminarAutor/<int:id>',views.eliminarAutor),
    path('actualizarAutor/<int:id>',views.actualizarAutor),
    path('agregar/',views.agregarLibro),
    path('libros/',views.listadoLibros),
    # el eliminar enviara el id y se pone tambien el tipo de dato
    path('eliminar/<int:id>',views.eliminarLibro),
    path('actualizar/<int:id>',views.actualizarLibro),

    # api
    path('autoresapi/',views.autor_list),
    path('autoresapi/<int:pk>',views.autor_detail),
    #nueva ruta
    path('accounts/',include('django.contrib.auth.urls')),
    
]
