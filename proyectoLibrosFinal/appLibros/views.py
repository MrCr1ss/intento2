from django.shortcuts import render, redirect
from . import forms
from .models import Autor, Libro

from .serializers import AutorSerializer,LibroSerializer
#Agregamos un filtro para iniciar sesión
from django.contrib.auth.decorators import login_required

# Vistas de Autor
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def agregarAutor(request):
    form=forms.RegistroAutorForm()
    if request.method=='POST':
        form=forms.RegistroAutorForm(request.POST)
        if form.is_valid():
            form.save()
            return listadoAutor(request)
    data={'form':form,'titulo':'Agregar'}
    return render(request,'agregarAutor.html',data)
@login_required
def listadoAutor(request):
    autores=Autor.objects.all()
    data={'autores':autores}
    return render(request,'autores.html',data)
@login_required
def eliminarAutor(request,id):
    autor=Autor.objects.get(autor_id=id)
    autor.delete()
    return redirect('/autores')
@login_required
def actualizarAutor(request,id):
    autor=Autor.objects.get(autor_id=id)
    form=forms.RegistroAutorForm(instance=autor)
    if request.method=='POST':
        form=forms.RegistroAutorForm(request.POST,instance=autor)
        if form.is_valid():
            form.save()
            return listadoAutor(request)
    data={'form':form,'titulo':'Actualizar'}
    return render(request,'agregarAutor.html',data)

#Fin vistas de autor

#Vistas Libro
@login_required
def listadoLibros(request):
    libros = Libro.objects.all()
    data = {'libros' : libros}
    return render(request, 'listado.html', data)
@login_required
def agregarLibro(request):
    form=forms.RegistroLibroForm()
    if request.method == 'POST':
        form=forms.RegistroLibroForm(request.POST)
        if form.is_valid():
            form.save()
            return listadoLibros(request)
    data={'form':form,'titulo':"Agregar"}
    return render(request,'Libro.html',data)

# importar redirect junto al render
@login_required
def eliminarLibro(request,id):
    libro=Libro.objects.get(libro_id=id)
    libro.delete()
    return redirect('/libros')
@login_required
def actualizarLibro(request,id):
    libro=Libro.objects.get(libro_id=id)
    form=forms.RegistroLibroForm(instance=libro)
    if request.method == 'POST':
        form=forms.RegistroLibroForm(request.POST,instance=libro)
        if form.is_valid():
            form.save()
            return listadoLibros(request)
    data={'form':form,'titulo':"Actualizar"}
    return render(request,'Libro.html',data)

#Para la API
#pip install djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET','POST'])

def autor_list(request):
    if request.method=='GET':
        autores=Autor.objects.all().order_by('autor_id')
        ser=AutorSerializer(autores,many=True)
        return Response(ser.data)
    if request.method=='POST':
        ser=AutorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def autor_detail(request,pk):
    try:
        autor=Autor.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        ser=AutorSerializer(autor)
        return Response (ser.data)
    if request.method=='PUT':
        ser=AutorSerializer(autor,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)