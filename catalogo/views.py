"""
Vistas de la app 'catalogo'.

Desde la Evaluación Sumativa #2 esta app consulta la base de datos
mediante el ORM de Django (Categoria.objects...) en lugar de leer
archivos JSON.
"""
from django.shortcuts import get_object_or_404, render

from .models import Categoria


def index(request):
    """Página de inicio: lista todas las categorías disponibles."""
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/index.html', {'categorias': categorias})


def categoria_detalle(request, categoria_id):
    """Muestra una categoría y los productos que pertenecen a ella."""
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    # select_related() evita una consulta extra por producto al acceder
    # a producto.categoria en la plantilla (JOIN en una sola query).
    productos = categoria.productos.select_related('categoria').all()

    contexto = {
        'categoria': categoria,
        'productos': productos,
    }
    return render(request, 'catalogo/categoria_detalle.html', contexto)
