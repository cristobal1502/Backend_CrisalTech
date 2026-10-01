from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/nueva/', views.categoria_crear, name='categoria_crear'),
    path('categoria/<int:categoria_id>/', views.categoria_detalle, name='categoria_detalle'),
    path('categoria/<int:categoria_id>/editar/', views.categoria_editar, name='categoria_editar'),
    path('categoria/<int:categoria_id>/eliminar/', views.categoria_eliminar, name='categoria_eliminar'),
]
