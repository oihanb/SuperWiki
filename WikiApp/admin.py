from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Editorial, GrupoDeSuperHeroes, SuperHeroe



class EditorialAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'propietario']}),
        ('Fundación', {'fields': ['anoFundacion']}),
        ('Imagen', {'fields': ['imagenEditorial']})
    ]
    
    list_display=('nombre','propietario','anoFundacion')
    #search_fields = ['nombre', 'propietario']
    #list_filter = ['anoFundacion']

admin.site.register(Editorial, EditorialAdmin)


class GrupoDeSuperHeroesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['nombre']}),
        ('Editorial',{'fields':['Editorial']})
    ]
    list_display=('nombre','Editorial')
    #list_filter = ['Editorial']
    #search_fields = ['nombre']
admin.site.register(GrupoDeSuperHeroes, GrupoDeSuperHeroesAdmin)

class SuperheroeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos Personales',{'fields':['nombre','Fnacimiento']}),
        ('Poderes',{'fields':['poderes']}),
        ('Imagen',{'fields':['imagenSuperHeroe']})
    ]
    list_display=('nombre','Fnacimiento','poderes')
    #search_fields = ['nombre', 'poderes']
admin.site.register(SuperHeroe, SuperheroeAdmin) 


