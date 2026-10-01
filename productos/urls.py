from django.urls import path

from . import views

app_name = 'productos'

urlpatterns = [
    path('nuevo/', views.producto_crear, name='producto_crear'),
    path('<int:producto_id>/', views.producto_detalle, name='producto_detalle'),
    path('<int:producto_id>/editar/', views.producto_editar, name='producto_editar'),
    path('<int:producto_id>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
]
