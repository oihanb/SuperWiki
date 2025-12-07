from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('inicio',views.index,name='index'),

    #LISTADO EDITORIALES
    #path('listaConfederaciones/', views.listaConfederacion,name='listaConfederacion'),
    path('listaeditorial/',views.listaEditorial.as_view(),name='listaeditorial'),
    #DETALLE DE EDITORIALES
    #path('detalleConfederacion/<int:id_confederacion>/', views.detalleConfederacion,name='detalleConfederacion'),
    path('detalleeditorial/<int:pk>', views.detalleEditorial.as_view(),name='detalleeditorial'),
    #LISTADO DE GRUPODESUPERHEROES
    #path('listaSelecciones/', views.listaSeleccion,name='listaSeleccion'),
    path('listagrupodesuperheroes/', views.listaGrupoDeSuperHeroes.as_view(),name='listagrupodesuperheroes'),
    #DETALLE DE GRUPODESUPERHEROES
    #path('detalleSeleccion/<int:id_seleccion>/', views.detalleSeleccion,name='detalleSeleccion'),
    path('detallegrupodesuperheroes/<int:pk>/', views.detalleGrupoDeSuperHeroes.as_view(),name='detallegrupodesuperheroes'),
    #LISTADO DE SUPERHEROE
    #path('listaFutbolistas/', views.listaFutbolista,name='listaFutbolista'),
    path('listasuperheroes/', views.listaSuperHeroe.as_view(),name='listasuperheroes'),
    #DETALLE DE SUPERHEROES
    #path('detalleFutbolista/<int:id_futbolista>/', views.detalleFutbolista,name='detalleFutbolista'),
    path('detallesuperheroes/<int:pk>/', views.detalleSuperHeroe.as_view(),name='detallesuperheroes'),
    # Contact page
    path('contact/', views.contact_view, name='contact'),
]