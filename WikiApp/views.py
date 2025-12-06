from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Editorial, GrupoDeSuperHeroes, SuperHeroe 

from django.views.generic import ListView,DetailView


# Vistas de lista
def index(request):
    return render(request, 'index.html')


#VISTAS EDITORIAL
class detalleEditorial(DetailView):
    model=Editorial
    template_name='detalleeditorial.html'
    context_object_name='editorial'

class listaEditorial(ListView):
    model= Editorial
    template_name='listaeditorial.html'
    context_object_name='editorial_list'

#VISTAS GRUPOSDESUPERHEROES
class detalleGrupoDeSuperHeroes(DetailView):
    model=GrupoDeSuperHeroes
    template_name='grupodesuperheroes.html'
    context_object_name='grupodesuperheroes'

class listaGrupoDeSuperHeroes(ListView):
    model= GrupoDeSuperHeroes
    template_name='listagrupodesuperheroes.html'
    context_object_name='grupodesuperheroes_list'

#VISTAS SUPERHEROES
class detalleSuperHeroe(DetailView):
    model=SuperHeroe
    template_name='detallesuperheroe.html'
    context_object_name='superheroe'

class listaSuperHeroe(ListView):
    model= SuperHeroe
    template_name='listasuperheroes.html'
    context_object_name='superheroes_list'
    queryset=SuperHeroe.objects.order_by('nombre')