from django import forms
from .models import SuperHeroe

class SuperHeroeForm(forms.ModelForm):
    class Meta:
        model = SuperHeroe
        fields = ['nombre', 'poderes', 'Fnacimiento', 'imagenSuperHeroe']
        labels = {
            'nombre': 'Superhero Name',
            'Fnacimiento': 'Año de Nacimiento (Año)',
        }
