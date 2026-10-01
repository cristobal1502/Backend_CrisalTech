"""
Configuración ASGI para el proyecto 'sitio_informativo'.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitio_informativo.settings')

application = get_asgi_application()
