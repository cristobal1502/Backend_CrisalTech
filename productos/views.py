"""
Vistas de la app 'productos'.

Desde la Evaluación Sumativa #2 esta app consulta la base de datos
mediante el ORM de Django (Producto.objects...) en lugar de leer
archivos JSON.
"""
from django.shortcuts import get_object_or_404, render

from .models import Producto


def producto_detalle(request, producto_id):
    """Muestra la ficha completa de un producto."""
    # select_related('categoria') resuelve el FK en la misma consulta.
    producto = get_object_or_404(
        Producto.objects.select_related('categoria'),
        pk=producto_id,
    )

    contexto = {
        'producto': producto,
        'categoria': producto.categoria,
    }
    return render(request, 'productos/producto_detalle.html', contexto)
