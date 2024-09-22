
from django.contrib import admin
from django.urls import path
from app_coder.views import crea_curso, lista_cursos, estudiantes, entregables, profesores, inicio  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crea_curso/<nombre>/<camada>', crea_curso),
    path('lista_curso/', lista_cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('inicio/', inicio),

]
