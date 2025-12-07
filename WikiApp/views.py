from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView, CreateView

from .forms import SuperHeroeForm
from .forms_contact import ContactForm
from .models import ContactMessage, Editorial, GrupoDeSuperHeroes, SuperHeroe



# Vistas de lista
def index(request):
    return render(request, 'WikiApp/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar en BD
            data = form.cleaned_data
            ContactMessage.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                message=data.get('message')
            )
            # Mostrar mensaje de éxito
            messages.success(request, _('Thank you for your message. We will get back to you soon.'))
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'WikiApp/contact.html', {'form': form})


#VISTAS EDITORIAL
class detalleEditorial(DetailView):
    model=Editorial
    template_name='WikiApp/detalleeditorial.html'
    context_object_name='editorial'

class listaEditorial(ListView):
    model= Editorial
    template_name='WikiApp/listaeditorial.html'
    context_object_name='editorial_list'

#VISTAS GRUPOSDESUPERHEROES
class detalleGrupoDeSuperHeroes(DetailView):
    model=GrupoDeSuperHeroes
    template_name='WikiApp/detallegrupodesuperheroes.html'
    context_object_name='grupodesuperheroes'

class listaGrupoDeSuperHeroes(ListView):
    model= GrupoDeSuperHeroes
    template_name='WikiApp/listagrupodesuperheroes.html'
    context_object_name='grupodesuperheroes_list'

#VISTAS SUPERHEROES
class detalleSuperHeroe(DetailView):
    model=SuperHeroe
    template_name='WikiApp/detallesuperheroe.html'
    context_object_name='superheroe'

class listaSuperHeroe(ListView):
    model= SuperHeroe
    template_name='WikiApp/listasuperheroes.html'
    context_object_name='superheroes_list'
    queryset=SuperHeroe.objects.order_by('nombre')

class SuperHeroeCreateView(CreateView):
    form_class = SuperHeroeForm 
    template_name = 'WikiApp/crearsuperheroe.html' 
    success_url = reverse_lazy('listasuperheroes')