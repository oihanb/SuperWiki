# WikiApp/urls.py (CONTENIDO FINAL Y CORRECTO)
from django.urls import path
from . import views

urlpatterns = [ # <-- Debe ser una lista
    path('', views.menu_principal, name='menu_principal'), 
    
    # Rutas de Listado
    path('superheroes/', views.superheroe_list, name='superheroe_list'),
    path('editoriales/', views.editorial_list, name='editorial_list'), 
    
    # Rutas de Grupos (Lista y Detalle)
    path('grupos/', views.grupo_list, name='grupo_list'), 
    
    # RUTA DETALLE: Debe estar dentro de la lista urlpatterns
    path('grupos/<int:grupo_id>/', views.grupo_detail, name='grupo_detail'), 
] # <-- La lista debe cerrarse aquí
