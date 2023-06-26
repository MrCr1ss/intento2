from django.db import models

# Create your models here.   

class Autor (models.Model):
    autor_id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30,verbose_name='Nombre')
    apellido=models.CharField(max_length=30, verbose_name='Apellido')  
    fechaNacimiento=models.DateField(verbose_name='Fecha de Nacimiento', null=True)
    nacionalidad=models.CharField(max_length=50, verbose_name='Nacionalidad')
    
    def nombre_autor(self):
        return "{} {}".format(self.nombre,self.apellido)
    
    def __str__(self):
        return self.nombre_autor()
    
class Libro(models.Model):
    libro_id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=30, verbose_name='Título')
    autor_id=models.ForeignKey(Autor, null=True,blank=True,on_delete=models.CASCADE, verbose_name='Autor')
    genero=models.CharField(max_length=15, verbose_name='Género')
    paginas=models.IntegerField(verbose_name='Páginas')
    descripcion=models.CharField(max_length=300, verbose_name='Descripción')
    
    def info_libro(self):
            return "{} {}".format(self.titulo,self.genero)
    
    def __str__(self):
        return self.info_libro()
    
    