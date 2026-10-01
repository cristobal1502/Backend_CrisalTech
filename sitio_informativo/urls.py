"""
Configuración de URLs del proyecto 'sitio_informativo'.

Se delega en cada aplicación (catalogo, productos) el manejo de sus propias
rutas mediante include(), manteniendo la arquitectura modular pedida.
"""
from django.urls import path, include

urlpatterns = [
    # App 1: catálogo -> categorías y listado de productos por categoría
    path('', include('catalogo.urls')),
    # App 2: productos -> ficha (detalle) de cada producto
    path('productos/', include('productos.urls')),
]
