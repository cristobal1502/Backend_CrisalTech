"""
Configuración de URLs del proyecto 'sitio_informativo'.

Se delega en cada aplicación (catalogo, productos) el manejo de sus propias
rutas mediante include(), manteniendo la arquitectura modular pedida.
"""
<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
=======
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
path('admin/', admin.site.urls),	
>>>>>>> 39f16a6712a5fdda68d8815c3f54e31a23c40f66
    # App 1: catálogo -> categorías y listado de productos por categoría
    path('', include('catalogo.urls')),
    # App 2: productos -> ficha (detalle) de cada producto
    path('productos/', include('productos.urls')),
]
