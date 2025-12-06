from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('inicio',views.index,name='index'),

    #LISTADO EDITORIALES
    #path('listaConfederaciones/', views.listaConfederacion,name='listaConfederacion'),
    path('listaEditoriales/',views.listaEditorial.as_view(),name='listaEditorial'),
    #DETALLE DE EDITORIALES
    #path('detalleConfederacion/<int:id_confederacion>/', views.detalleConfederacion,name='detalleConfederacion'),
    path('detalleEditorial/<int:pk>', views.detalleEditorial.as_view(),name='detalleEditorial'),
    #LISTADO DE GRUPODESUPERHEROES
    #path('listaSelecciones/', views.listaSeleccion,name='listaSeleccion'),
    path('listagrupodesuperheroes/', views.listaGrupoDeSuperHeroes.as_view(),name='listaGrupoDeSuperHeroes'),
    #DETALLE DE GRUPODESUPERHEROES
    #path('detalleSeleccion/<int:id_seleccion>/', views.detalleSeleccion,name='detalleSeleccion'),
    path('detalleGrupoDeSuperHeroes/<int:pk>/', views.detalleGrupoDeSuperHeroes.as_view(),name='detalleGrupoDeSuperHeroes'),
    #LISTADO DE SUPERHEROE
    #path('listaFutbolistas/', views.listaFutbolista,name='listaFutbolista'),
    path('listaSuperHeroes/', views.listaSuperHeroe.as_view(),name='listaSuperHeroes'),
    #DETALLE DE SUPERHEROES
    #path('detalleFutbolista/<int:id_futbolista>/', views.detalleFutbolista,name='detalleFutbolista')
    path('detalleSuperHeroes/<int:pk>/', views.detalleSuperHeroe.as_view(),name='detalleSuperHeroe')
]