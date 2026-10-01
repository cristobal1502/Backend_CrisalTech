from django.db import models

from catalogo.models import Categoria


class Producto(models.Model):
    """
    Representa la ficha de un producto.
    Reemplaza la estructura que antes vivía en productos/data/productos.json.
    Se relaciona con Categoria (app 'catalogo') mediante ForeignKey.
    """

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name='Categoría',
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField(default=0)
    # Ruta relativa dentro de /static/ (ej: 'img/producto_generico.svg').
    imagen = models.CharField(
        max_length=300,
        blank=True,
        help_text="Ruta dentro de static/, ej: img/producto_generico.svg",
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.categoria.nombre})'

    @property
    def en_stock(self):
        return self.stock > 0
