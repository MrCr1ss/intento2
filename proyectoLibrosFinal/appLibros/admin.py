from django.contrib import admin
from .models import Autor,Libro

class infoLibro(admin.ModelAdmin):
    list_display=['titulo','genero']

# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)
