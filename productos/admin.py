from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock', 'en_stock')
    search_fields = ('nombre', 'descripcion', 'categoria__nombre')
    list_filter = ('categoria', 'stock')
    ordering = ('nombre',)
    # Permite ver y navegar directamente a la categoría relacionada
    # desde el listado de productos (autocompletado por FK).
    autocomplete_fields = ('categoria',)
    list_select_related = ('categoria',)

    @admin.display(boolean=True, description='¿En stock?')
    def en_stock(self, producto):
        return producto.stock > 0
