from django.contrib import admin
from .models import Editorial, GrupoDeSuperHeroes, SuperHeroe

# 1. Creamos una clase personalizada para la administración del Grupo
class GrupoDeSuperHeroesAdmin(admin.ModelAdmin):
    # Usamos filter_horizontal para mostrar la relación Many-to-Many 
    # de forma gráfica, permitiendo seleccionar fácilmente múltiples elementos.
    filter_horizontal = ('SuperHeroe',) 
    # El nombre 'SuperHeroe' es el nombre del campo ManyToMany en models.py
    
# 2. Registramos el modelo usando nuestra clase personalizada
admin.site.register(Editorial)
admin.site.register(GrupoDeSuperHeroes, GrupoDeSuperHeroesAdmin)
admin.site.register(SuperHeroe)