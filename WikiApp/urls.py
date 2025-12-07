from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('inicio',views.index,name='index'),

    #LISTADO EDITORIALES
    path('listaeditorial/',views.listaEditorial.as_view(),name='listaeditorial'),
    #DETALLE DE EDITORIALES
    path('detalleeditorial/<int:pk>', views.detalleEditorial.as_view(),name='detalleeditorial'),
    #LISTADO DE GRUPODESUPERHEROES
    path('listagrupodesuperheroes/', views.listaGrupoDeSuperHeroes.as_view(),name='listagrupodesuperheroes'),
    #DETALLE DE GRUPODESUPERHEROES
    path('detallegrupodesuperheroes/<int:pk>/', views.detalleGrupoDeSuperHeroes.as_view(),name='detallegrupodesuperheroes'),
    #LISTADO DE SUPERHEROE
    path('listasuperheroes/', views.listaSuperHeroe.as_view(),name='listasuperheroes'),
    #DETALLE DE SUPERHEROES
    path('detallesuperheroes/<int:pk>/', views.detalleSuperHeroe.as_view(),name='detallesuperheroes'),
    #CREAR SUPERHEROE
    path('crearsuperheroe/', views.SuperHeroeCreateView.as_view(), name='crearsuperheroe'),
]