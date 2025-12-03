from django.contrib import admin
from .models import Editorial, GrupoDeSuperHeroes, SuperHeroe

# Clase para el filtro Many-to-Many
class GrupoDeSuperHeroesAdmin(admin.ModelAdmin):
    filter_horizontal = ('SuperHeroe',)

# CLASE NUEVA para personalizar permisos en SuperHeroe
class SuperheroeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'poderes', 'Fnacimiento') # Pequeña mejora visual
    
    # Lógica para permisos (Asumiendo que existe un grupo 'Administradores')
    def has_change_permission(self, request, obj=None):
        # Permite la edición si es Superuser O si pertenece al grupo 'Administradores'
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Administradores').exists()
    
    def has_delete_permission(self, request, obj=None):
        # Los mismos permisos para eliminar
        return self.has_change_permission(request, obj)
    
    def has_add_permission(self, request):
        # Los mismos permisos para añadir (opcional, pero consistente)
        return self.has_change_permission(request)

# Registro de Modelos con las clases personalizadas
admin.site.register(Editorial)
admin.site.register(GrupoDeSuperHeroes, GrupoDeSuperHeroesAdmin)
admin.site.register(SuperHeroe, SuperheroeAdmin) # ¡Registrado con la clase personalizada!