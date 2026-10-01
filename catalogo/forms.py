from django import forms

from .models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Electrónica',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Breve descripción de la categoría',
            }),
            'imagen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'img/categoria_electronica.svg',
            }),
        }
