"""
Vistas de la app 'catalogo'.

Incluye el listado/búsqueda de categorías y el CRUD completo
(crear, editar, eliminar) sobre el modelo Categoria, usando ModelForm.
"""
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm
from .models import Categoria


def index(request):
    """Página de inicio: lista las categorías, con búsqueda opcional (?q=...)."""
    query = request.GET.get('q', '').strip()

    categorias = Categoria.objects.all()
    if query:
        categorias = categorias.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )

    contexto = {'categorias': categorias, 'query': query}
    return render(request, 'catalogo/index.html', contexto)


def categoria_detalle(request, categoria_id):
    """Muestra una categoría y los productos que pertenecen a ella, con búsqueda opcional."""
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    query = request.GET.get('q', '').strip()

    productos = categoria.productos.select_related('categoria').all()
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )

    contexto = {'categoria': categoria, 'productos': productos, 'query': query}
    return render(request, 'catalogo/categoria_detalle.html', contexto)


def categoria_crear(request):
    """Crea una nueva categoría a partir del formulario (botón 'Agregar categoría')."""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, f'Categoría "{categoria.nombre}" creada correctamente.')
            return redirect('catalogo:index')
    else:
        form = CategoriaForm()

    return render(request, 'catalogo/categoria_form.html', {'form': form, 'modo': 'crear'})


def categoria_editar(request, categoria_id):
    """Edita una categoría existente (botón 'Modificar')."""
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, f'Categoría "{categoria.nombre}" actualizada correctamente.')
            return redirect('catalogo:index')
    else:
        form = CategoriaForm(instance=categoria)

    contexto = {'form': form, 'modo': 'editar', 'categoria': categoria}
    return render(request, 'catalogo/categoria_form.html', contexto)


def categoria_eliminar(request, categoria_id):
    """Elimina una categoría, con pantalla de confirmación (botón 'Eliminar')."""
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method == 'POST':
        nombre = categoria.nombre
        categoria.delete()
        messages.success(request, f'Categoría "{nombre}" eliminada correctamente.')
        return redirect('catalogo:index')

    return render(request, 'catalogo/categoria_confirm_delete.html', {'categoria': categoria})
