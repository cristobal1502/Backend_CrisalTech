from django.db import models


class Categoria(models.Model):
    """
    Representa una categoría del catálogo de productos.
    Reemplaza la estructura que antes vivía en catalogo/data/categorias.json.
    """

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    # Ruta relativa dentro de /static/ (ej: 'img/categoria_electronica.svg').
    # Se mantiene como CharField -para no requerir MEDIA_ROOT ni Pillow-,
    # igual que en la versión basada en JSON.
    imagen = models.CharField(
        max_length=300,
        blank=True,
        help_text="Ruta dentro de static/, ej: img/categoria_electronica.svg",
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
