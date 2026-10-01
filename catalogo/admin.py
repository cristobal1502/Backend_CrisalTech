from django.contrib import admin

from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'cantidad_productos')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)
    ordering = ('nombre',)

    @admin.display(description='N° de productos')
    def cantidad_productos(self, categoria):
        # Navegación clara hacia la entidad relacionada (Producto),
        # usando el related_name='productos' definido en el FK.
        return categoria.productos.count()
