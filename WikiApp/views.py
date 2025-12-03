from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView # Nuevas importaciones
from .models import Editorial, GrupoDeSuperHeroes, SuperHeroe 

# 1. MENÚ PRINCIPAL (TemplateView)
class MenuPrincipalView(TemplateView):
    template_name = 'WikiApp/menu_principal.html'

# 2. LISTA DE SUPERHÉROES (ListView)
class SuperheroeListView(ListView):
    model = SuperHeroe
    template_name = 'WikiApp/lista_superheroes.html'
    context_object_name = 'superheroes' # Nombre usado en la plantilla

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Lista Completa de Superhéroes'
        return context

# 3. LISTA DE EDITORIALES (ListView)
class EditorialListView(ListView):
    model = Editorial
    template_name = 'WikiApp/editorial_list.html'
    context_object_name = 'editoriales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Editoriales'
        return context

# 4. LISTA DE GRUPOS (ListView)
class GrupoListView(ListView):
    model = GrupoDeSuperHeroes
    template_name = 'WikiApp/grupo_list.html'
    context_object_name = 'grupos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de Grupos de Superhéroes'
        return context
    
# 5. VISTA DE DETALLE DEL GRUPO (DetailView)
class GrupoDetailView(DetailView):
    model = GrupoDeSuperHeroes
    template_name = 'WikiApp/grupo_detail.html'
    pk_url_kwarg = 'grupo_id' # Usa el nombre del parámetro en la URL
    context_object_name = 'grupo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo = self.get_object()
        context['superheroes'] = grupo.SuperHeroe.all() # Acceso a miembros
        context['titulo_pagina'] = f'Miembros de: {grupo.nombre}'
        return context

# 6. VISTA DE FILTRADO (Se mantiene como Función-Basada por la lógica de filtrado personalizada)
def editorial_grupos(request, editorial_id):
    editorial = get_object_or_404(Editorial, pk=editorial_id)
    grupos = editorial.editorialGrupo.all() 
    contexto = {
        'grupos': grupos,
        'titulo_pagina': f'Grupos de la Editorial: {editorial.nombre}'
    }
    return render(request, 'WikiApp/grupo_list.html', contexto)
def superheroe_json(request, heroe_id):
    heroe = get_object_or_404(SuperHeroe, pk=heroe_id)
    
    # Devolver datos en formato JSON
    data = {
        'nombre': heroe.nombre,
        'poderes': heroe.poderes,
        'nacimiento': heroe.Fnacimiento,
        'foto_url': heroe.foto if heroe.foto else None
    }
    return JsonResponse(data)