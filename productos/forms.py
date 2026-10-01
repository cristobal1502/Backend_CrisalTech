from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Audífonos inalámbricos',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Breve descripción del producto',
            }),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'imagen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'img/producto_generico.svg',
            }),
        }
