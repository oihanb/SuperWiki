# WikiApp/urls.py (CONTENIDO ACTUALIZADO)
from django.urls import path
from . import views

urlpatterns=[
    # 1. La página raíz (http://127.0.0.1:8000/WikiApp/) ahora es el menú
    path('', views.menu_principal, name='menu_principal'), 
    
    # 2. Rutas para las listas de modelos
    path('superheroes/', views.superheroe_list, name='superheroe_list'),
    path('editoriales/', views.editorial_list, name='editorial_list'), 
    path('grupos/', views.grupo_list, name='grupo_list'), 
]