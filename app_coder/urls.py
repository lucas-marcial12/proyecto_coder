
from django.contrib import admin
from django.urls import path
from app_coder.views import *  

urlpatterns = [
    path('crea_curso/<nombre>/<camada>', crea_curso),
    path('lista_curso/', lista_cursos, name= 'lista_curso'),
    path('profesores/', profesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('entregables/', entregables, name= 'entregables'),
    path('', inicio),
    path('curso_formulario', curso_formulario, name= 'curso_formulario'),

]
