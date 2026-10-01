# Sitio Informativo de Productos (Django + MySQL)

Proyecto académico desarrollado con **Django**, usando **MySQL/MariaDB** como
base de datos a través del **ORM**, variables de entorno (`.env`) y una
interfaz en **Bootstrap local**, con **herencia de plantillas**.

> Esta es la versión 2 del proyecto (Evaluación Sumativa #2). La versión
> anterior leía datos desde archivos `.json`; ahora esa información vive en
> modelos relacionales en MySQL, gestionados vía Django ORM y admin.

## Arquitectura

| App         | Responsabilidad                                                        |
|-------------|--------------------------------------------------------------------------|
| `catalogo`  | Modelo `Categoria`. Página de inicio con las categorías y, para cada una, el listado de productos que contiene (vía ORM). |
| `productos` | Modelo `Producto` (con `ForeignKey` a `Categoria`). Ficha de detalle de cada producto. |

### Modelo de datos

```
Categoria (catalogo)                 Producto (productos)
├── id                                ├── id
├── nombre                            ├── categoria_id  (FK -> Categoria)
├── descripcion                       ├── nombre
└── imagen                            ├── descripcion
                                       ├── precio
                                       ├── stock
                                       └── imagen
```

### Herencia de plantillas

- `templates/base.html` → plantilla base del proyecto (navbar, footer, enlaces
  a Bootstrap local y CSS propio).
- Todas las demás plantillas heredan con `{% extends 'base.html' %}`.

### Controles CRUD en las vistas de listado

`catalogo/index.html` y `catalogo/categoria_detalle.html` incluyen una
barra con los 4 controles pedidos: **Agregar**, **Buscar**, y por cada
tarjeta **Modificar** / **Eliminar**. Por ahora apuntan a `#` (rutas
provisionales); la lógica de backend (crear/editar/eliminar) se implementará
en una siguiente iteración.

## Estructura de carpetas

```
sitio_informativo/
├── manage.py
├── requirements.txt
├── .env                       # tus credenciales reales (NO se sube a git)
├── .env.example                # plantilla de referencia
├── sitio_informativo/          # configuración del proyecto (settings, urls)
├── catalogo/
│   ├── models.py               # modelo Categoria
│   ├── admin.py                # CategoriaAdmin
│   ├── views.py                # consultas ORM
│   ├── fixtures/categorias_initial.json   # datos semilla
│   └── templates/catalogo/
├── productos/
│   ├── models.py                # modelo Producto (FK a Categoria)
│   ├── admin.py                 # ProductoAdmin
│   ├── views.py                 # consultas ORM
│   ├── fixtures/productos_initial.json    # datos semilla
│   └── templates/productos/
├── templates/base.html          # plantilla base (herencia)
└── static/
    ├── bootstrap/css/           # <-- aquí va bootstrap.min.css
    ├── bootstrap/js/            # <-- aquí va bootstrap.bundle.min.js
    ├── css/estilos.css
    └── img/                     # placeholders SVG
```

## ⚠️ Paso obligatorio: Bootstrap local

Descarga los archivos compilados desde
https://getbootstrap.com/docs/5.3/getting-started/download/ y copia:

- `bootstrap.min.css` → `static/bootstrap/css/bootstrap.min.css`
- `bootstrap.bundle.min.js` → `static/bootstrap/js/bootstrap.bundle.min.js`

## ⚠️ Paso obligatorio: archivo `.env`

El proyecto ya incluye un `.env` de ejemplo funcional. Ábrelo y ajusta al
menos `DB_PASSWORD` con la contraseña real de tu usuario MySQL/MariaDB:

```env
SECRET_KEY=django-insecure-cambia-esta-clave-por-una-generada-para-produccion
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.mysql
DB_NAME=sitio_informativo_db
DB_USER=root
DB_PASSWORD=TU_CONTRASEÑA_AQUI
DB_HOST=127.0.0.1
DB_PORT=3306
```

**Nunca subas el `.env` real a tu repositorio** — ya está en `.gitignore`.
Si tu profesor pide ver la plantilla, comparte `.env.example`.

## Base de datos: crearla antes de migrar

Django **no crea la base de datos** por ti, solo las tablas dentro de ella.
Antes de migrar, crea la base vacía (con el mismo nombre que pusiste en
`DB_NAME`) desde phpMyAdmin o por consola:

```sql
CREATE DATABASE sitio_informativo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Instalación y ejecución — comandos exactos

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear las migraciones a partir de los modelos
python manage.py makemigrations catalogo
python manage.py makemigrations productos

# 4. Aplicar las migraciones (crea las tablas en MySQL -> visibles en phpMyAdmin)
python manage.py migrate

# 5. (Opcional pero recomendado) Cargar los datos semilla
python manage.py loaddata categorias_initial
python manage.py loaddata productos_initial

# 6. Crear un superusuario para entrar al panel /admin/
python manage.py createsuperuser

# 7. Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abre:
- Sitio público: `http://127.0.0.1:8000/`
- Panel de administración: `http://127.0.0.1:8000/admin/`

## Problemas comunes al instalar `mysqlclient` en Windows

Si `pip install -r requirements.txt` falla en `mysqlclient` (es común en
Windows por requerir compiladores de C), usa esta alternativa:

```bash
pip install pymysql
```

Y agrega estas dos líneas al inicio de `sitio_informativo/__init__.py`:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

Esto hace que Django use `PyMySQL` como si fuera `mysqlclient`, sin tocar
`settings.py` ni el resto del proyecto.

## Nota sobre el uso de IA Generativa

Este proyecto fue desarrollado con apoyo de una herramienta de Inteligencia
Artificial Generativa (Claude, de Anthropic), utilizada como asistente
durante el proceso de desarrollo para generar y estructurar el código,
conforme lo solicita el enunciado de la actividad.
