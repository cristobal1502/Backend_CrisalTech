# Sitio Informativo de Productos (Django + MySQL en la nube)

Proyecto académico desarrollado con **Django**, usando **MySQL/MariaDB**
alojado en una instancia en la nube como base de datos (vía ORM), variables
de entorno (`.env`), **Bootstrap vía CDN** y **herencia de plantillas**.

## Arquitectura

| App         | Responsabilidad                                                        |
|-------------|--------------------------------------------------------------------------|
| `catalogo`  | Modelo `Categoria`. Página de inicio con las categorías, listado de productos por categoría, y CRUD completo de categorías. |
| `productos` | Modelo `Producto` (con `ForeignKey` a `Categoria`). Ficha de detalle y CRUD completo de productos. |

Además, `django.contrib.admin` está habilitado en `/admin/` para gestionar
ambos modelos desde el panel de administración de Django.

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

### Bootstrap vía CDN

A diferencia de una versión anterior de este proyecto, Bootstrap **no** se
sirve localmente: se carga desde el CDN de jsDelivr en `templates/base.html`:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
...
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
```

> ⚠️ Si tu pauta de evaluación exige explícitamente "Bootstrap de forma
> local", este cambio no la cumple. Verifícalo con tu profesor si aplica.

### Herencia de plantillas

- `templates/base.html` → plantilla base (navbar, footer, Bootstrap CDN,
  mensajes de confirmación del CRUD).
- Todas las demás plantillas heredan con `{% extends 'base.html' %}`.

### CRUD funcional

Los 4 controles (Agregar / Modificar / Eliminar / Buscar) están conectados
a vistas reales, no a rutas provisionales:

| Acción | Categoría | Producto |
|---|---|---|
| Agregar | `catalogo:categoria_crear` | `productos:producto_crear` |
| Modificar | `catalogo:categoria_editar` | `productos:producto_editar` |
| Eliminar | `catalogo:categoria_eliminar` | `productos:producto_eliminar` |
| Buscar | `?q=` en `catalogo:index` | `?q=` en `catalogo:categoria_detalle` |

Todas usan `ModelForm` (`catalogo/forms.py`, `productos/forms.py`) y muestran
confirmaciones vía `django.contrib.messages`.

## ⚠️ Archivo `.env`

Tu `.env` real (con `DB_HOST`, `DB_USER`, `DB_PASSWORD` de la instancia en
la nube) **no está incluido en este paquete** — ya lo tienes localmente y
está correctamente en `.gitignore`. No lo sobrescribas con `.env.example`.

```env
SECRET_KEY=...
DEBUG=True
ALLOWED_HOSTS=3.94.106.128,localhost,127.0.0.1

DB_ENGINE=django.db.backends.mysql
DB_NAME=sitio_informativo_db
DB_USER=tu_usuario
DB_PASSWORD=tu_password_real
DB_HOST=3.94.106.128
DB_PORT=3306
```

`settings.py` ya **no** tiene valores de contraseña por defecto: si falta
`DB_PASSWORD` en el `.env`, Django fallará claramente en vez de usar un
valor oculto en el código.

## Instalación y ejecución

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations catalogo
python manage.py makemigrations productos
python manage.py migrate

# Datos de ejemplo (opcional)
python manage.py loaddata categorias_initial
python manage.py loaddata productos_initial

python manage.py createsuperuser
python manage.py runserver
```

- Sitio público: `http://127.0.0.1:8000/`
- Panel de administración: `http://127.0.0.1:8000/admin/`

## Nota sobre el uso de IA Generativa

Este proyecto fue desarrollado con apoyo de una herramienta de Inteligencia
Artificial Generativa (Claude, de Anthropic), utilizada como asistente
durante el proceso de desarrollo para generar y estructurar el código,
conforme lo solicita el enunciado de la actividad.
