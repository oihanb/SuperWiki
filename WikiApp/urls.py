# WikiApp/urls.py (CONTENIDO ACTUALIZADO)
from django.urls import path
from . import views

urlpatterns=[
    path('', views.MenuPrincipalView.as_view(), name='menu_principal'), 
    
    path('superheroes/', views.SuperheroeListView.as_view(), name='superheroe_list'),
    path('editoriales/', views.EditorialListView.as_view(), name='editorial_list'), 
    
    path('editoriales/<int:editorial_id>/', views.editorial_grupos, name='editorial_grupos'), # FBV se mantiene
    
    path('grupos/', views.GrupoListView.as_view(), name='grupo_list'), 
    path('grupos/<int:grupo_id>/', views.GrupoDetailView.as_view(), name='grupo_detail'), 
    path('api/superheroes/<int:heroe_id>/', views.superheroe_json, name='superheroe_json'),
]
