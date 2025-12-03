# WikiApp/urls.py (CONTENIDO FINAL Y CORRECTO)
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.menu_principal, name='menu_principal'), 
    
    path('superheroes/', views.superheroe_list, name='superheroe_list'),
    path('editoriales/', views.editorial_list, name='editorial_list'), 
    
    # RUTA NUEVA: DETALLE DE GRUPOS POR EDITORIAL (La que fallaba)
    path('editoriales/<int:editorial_id>/', views.editorial_grupos, name='editorial_grupos'),

    path('grupos/', views.grupo_list, name='grupo_list'), 
    path('grupos/<int:grupo_id>/', views.grupo_detail, name='grupo_detail'), 
]
