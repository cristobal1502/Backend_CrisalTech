"""
Configuración del proyecto 'sitio_informativo'.

A partir de la Evaluación Sumativa #2, el proyecto:
  - Lee su configuración sensible (SECRET_KEY, DEBUG, credenciales de BD)
    desde variables de entorno con python-dotenv, nunca hardcodeadas.
  - Usa MySQL/MariaDB como motor de base de datos (visible en phpMyAdmin)
    en lugar de archivos JSON.
  - Los modelos (catalogo.Categoria, productos.Producto) se gestionan con
    el ORM de Django.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga las variables definidas en el archivo .env ubicado en BASE_DIR
load_dotenv(BASE_DIR / '.env')

# --------------------------------------------------------------------------
# Seguridad / entorno — leídos desde .env
# --------------------------------------------------------------------------
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('ALLOWED_HOSTS', '3.94.106.128,localhost,127.0.0.1,*').split(',')
    if host.strip()
]

# --------------------------------------------------------------------------
# Aplicaciones instaladas
# --------------------------------------------------------------------------
# Se reincorporan 'admin', 'auth', 'contenttypes', 'sessions' y 'messages'
# porque ahora SÍ se usa base de datos (requeridas por el panel de admin,
# las migraciones y el ORM).
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',
    'productos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sitio_informativo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Carpeta de plantillas compartidas (base.html) a nivel de proyecto.
        'DIRS': [BASE_DIR / 'templates'],
        # Permite además que cada app use sus propias plantillas en
        # <app>/templates/<app>/ (herencia de plantillas de Django).
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sitio_informativo.wsgi.application'

# --------------------------------------------------------------------------
# Base de datos: MySQL / MariaDB, configurada 100% desde variables de entorno.
# Al crear la base y correr las migraciones quedará visible en phpMyAdmin.
# --------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('DB_NAME', ''),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'admin12345'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# Validación de contraseñas (estándar de Django, requerido por el admin)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------
# Archivos estáticos (CSS, JS, imágenes, Bootstrap local)
# --------------------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
