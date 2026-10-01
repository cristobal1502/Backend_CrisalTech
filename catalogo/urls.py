from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/<int:categoria_id>/', views.categoria_detalle, name='categoria_detalle'),
]
