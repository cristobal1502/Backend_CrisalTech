"""
Vistas de la app 'productos'.

Incluye la ficha de detalle y el CRUD completo (crear, editar, eliminar)
sobre el modelo Producto, usando ModelForm.
"""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.models import Categoria

from .forms import ProductoForm
from .models import Producto


def producto_detalle(request, producto_id):
    """Muestra la ficha completa de un producto."""
    producto = get_object_or_404(
        Producto.objects.select_related('categoria'),
        pk=producto_id,
    )
    contexto = {'producto': producto, 'categoria': producto.categoria}
    return render(request, 'productos/producto_detalle.html', contexto)


def producto_crear(request):
    """
    Crea un nuevo producto (botón 'Agregar producto' en la vista de categoría).
    Si se llega desde categoria_detalle, ?categoria=<id> precarga esa categoría.
    """
    categoria_id = request.GET.get('categoria')
    categoria_inicial = (
        Categoria.objects.filter(pk=categoria_id).first() if categoria_id else None
    )

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" creado correctamente.')
            return redirect('catalogo:categoria_detalle', categoria_id=producto.categoria_id)
    else:
        initial = {'categoria': categoria_inicial} if categoria_inicial else {}
        form = ProductoForm(initial=initial)

    return render(request, 'productos/producto_form.html', {'form': form, 'modo': 'crear'})


def producto_editar(request, producto_id):
    """Edita un producto existente (botón 'Modificar')."""
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado correctamente.')
            return redirect('productos:producto_detalle', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)

    contexto = {'form': form, 'modo': 'editar', 'producto': producto}
    return render(request, 'productos/producto_form.html', contexto)


def producto_eliminar(request, producto_id):
    """Elimina un producto, con pantalla de confirmación (botón 'Eliminar')."""
    producto = get_object_or_404(Producto, pk=producto_id)
    categoria_id = producto.categoria_id

    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado correctamente.')
        return redirect('catalogo:categoria_detalle', categoria_id=categoria_id)

    return render(request, 'productos/producto_confirm_delete.html', {'producto': producto})
