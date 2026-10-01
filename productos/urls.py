from django.urls import path

from . import views

app_name = 'productos'

urlpatterns = [
    path('<int:producto_id>/', views.producto_detalle, name='producto_detalle'),
]
