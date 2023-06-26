from django import forms
from appLibros.models import Libro, Autor


class RegistroAutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields='__all__'


nombre=forms.CharField()
apellido=forms.CharField()  
fechaNacimiento=forms.DateTimeField(widget=forms.DateTimeInput)
nacionalidad=forms.CharField()

nombre.widget.attrs['class']='form-control'
apellido.widget.attrs['class']='form-control'
fechaNacimiento.widget.attrs['class']='form-control datetimepicker-input'
nacionalidad.widget.attrs['class']='form-control'

#Libros

#Libros

class RegistroLibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields='__all__'
        
titulo=forms.CharField()
# autor_id=forms.ForeignKey()
# autor=forms.CharField(widget=forms.Select(Autor.objects.all().values_list('nombre')))
genero=forms.CharField()
paginas=forms.IntegerField(min_value=1)
descripcion=forms.CharField()
    
titulo.widget.attrs['class']='form-control'
genero.widget.attrs['class']='form-control'
paginas.widget.attrs['class']='form-control'
descripcion.widget.attrs['class']='form-control'
    
        
   
    


