from django import forms
from .models import SuperHeroe
from django.utils.translation import gettext_lazy as _

class SuperHeroeForm(forms.ModelForm):
    class Meta:
        model = SuperHeroe
        fields = ['nombre', 'poderes', 'Fnacimiento', 'imagenSuperHeroe']
        labels = {
            'nombre': _('Name'),
            'poderes': _('Powers'),
            'Fnacimiento': _('Birth Year (Year)'),
            'imagenSuperHeroe': _('Superhero Image'),
        }
