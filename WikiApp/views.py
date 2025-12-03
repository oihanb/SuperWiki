from django.shortcuts import render
from .models import SuperHeroe  # 1. Importar el modelo

# La función index ahora carga los datos y renderiza una plantilla
def index(request):
    # 2. Recuperar todos los objetos SuperHeroe de la base de datos
    lista_superheroes = SuperHeroe.objects.all()

    # 3. Crear el contexto para enviar los datos a la plantilla
    contexto = {
        'superheroes': lista_superheroes,
        'titulo_pagina': 'Lista de Superhéroes'
    }

    # 4. Renderizar la plantilla 'lista_superheroes.html'
    return render(request, 'WikiApp/lista_superheroes.html', contexto)