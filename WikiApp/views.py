from django.shortcuts import render, get_object_or_404
from .models import Editorial, GrupoDeSuperHeroes, SuperHeroe 

# 1. VISTA DEL MENÚ PRINCIPAL
def menu_principal(request):
    return render(request, 'WikiApp/menu_principal.html', {})

# 2. VISTA DE LA LISTA DE SUPERHÉROES
def superheroe_list(request):
    lista_superheroes = SuperHeroe.objects.all()
    contexto = {
        'superheroes': lista_superheroes,
        'titulo_pagina': 'Lista Completa de Superhéroes'
    }
    return render(request, 'WikiApp/lista_superheroes.html', contexto)

# 3. VISTA DE LA LISTA DE EDITORIALES
def editorial_list(request):
    editoriales = Editorial.objects.all()
    contexto = {'editoriales': editoriales, 'titulo_pagina': 'Listado de Editoriales'}
    return render(request, 'WikiApp/editorial_list.html', contexto) 


# 4. VISTA DE LA LISTA DE GRUPOS
def grupo_list(request):
    grupos = GrupoDeSuperHeroes.objects.all()
    contexto = {'grupos': grupos, 'titulo_pagina': 'Listado de Grupos de Superhéroes'}
    return render(request, 'WikiApp/grupo_list.html', contexto) 


# 5. VISTA DE DETALLE DEL GRUPO (La que estaba causando el error)
def grupo_detail(request, grupo_id):
    grupo = get_object_or_404(GrupoDeSuperHeroes, pk=grupo_id)
    
    # Se obtienen los miembros del grupo (relación Many-to-Many)
    superheroes_del_grupo = grupo.SuperHeroe.all()
    
    contexto = {
        'grupo': grupo,
        'superheroes': superheroes_del_grupo,
        'titulo_pagina': f'Miembros de: {grupo.nombre}'
    }
    return render(request, 'WikiApp/grupo_detail.html', contexto)