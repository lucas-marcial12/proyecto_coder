from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import curso
# Create your views here.

def crea_curso(req, nombre, camada):
    nuevo_curso = curso(nombre = nombre, camada = camada)
    nuevo_curso.save()

    return HttpResponse(f"""
        <p> Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado con exito</p>              
                        
                        
                     """)

def lista_cursos(req):
    lista = curso.objects.all()

    return render(req, 'lista_cursos.html', {'lista_cursos': lista})