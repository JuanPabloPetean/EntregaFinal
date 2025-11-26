# Entrega3 — Teatro Proyecto

Aplicación Django para gestionar obras de teatro.

## Datos personales

- Nombre: Juan Pablo Petean
- Curso: Programación en Python
- Tema: Entrega 3: Página web de obra de teatro

## Requisitos

- Python 3.13+
- Django 5.2.8

## Instalación

1. **Clonar el repositorio:**
```bash
git clone <url-repositorio>
cd teatro_proyecto
```

2. **Crear entorno virtual (si no existe):**
```bash
python -m venv venv
```

3. **Activar entorno virtual:**

En Windows (PowerShell):
```powershell
.\venv\Scripts\Activate
```

En Mac/Linux:
```bash
source venv/bin/activate
```

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

5. **Aplicar migraciones:**
```bash
python manage.py migrate
```

6. **Crear superusuario (admin):**
```bash
python manage.py createsuperuser
```

## Ejecución

Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

El servidor estará disponible en:
- **App**: http://127.0.0.1:8000/obras/
- **Admin**: http://127.0.0.1:8000/admin/

## Nuevas funcionalidades añadidas

Se agregó la posibilidad de crear obras desde la propia aplicación web además del panel de administración.

- **URL de creación:** `http://127.0.0.1:8000/obras/nueva/`
- **Vista:** `crear_obra` en `teatro/views.py` (maneja GET/POST)
- **Formulario:** `ObraForm` en `teatro/forms.py` (ModelForm del modelo `Obra`)
- **Plantilla de creación:** `templates/teatro/crear_obra.html`
- **Plantilla de lista:** `templates/teatro/lista_obras.html` (actualizada con enlace para crear obras y con más campos mostrados)

Al enviar el formulario se guarda la obra y se redirige a la lista de obras (`/obras/`).

## Archivos añadidos / modificados

- `teatro/forms.py` — `ObraForm` (ModelForm)
- `teatro/views.py` — nueva vista `crear_obra`
- `teatro/urls.py` — nueva ruta `path('obras/nueva/', views.crear_obra, name='crear_obra')`
- `templates/teatro/crear_obra.html` — plantilla para el formulario
- `templates/teatro/lista_obras.html` — actualizado con enlace y más campos mostrados

## Probar la funcionalidad

1. Arranca el servidor:
```powershell
python manage.py runserver
```
2. Visita `http://127.0.0.1:8000/obras/nueva/` y completa el formulario.
3. Tras enviar el formulario verás la nueva obra listada en `http://127.0.0.1:8000/obras/`.

Si prefieres usar el panel administrativo en su lugar, el modelo `Obra` ya está registrado en el admin (`http://127.0.0.1:8000/admin/`).

## Estructura del Proyecto

```
teatro_proyecto/
├── teatro/                  # Aplicación principal
│   ├── migrations/          # Migraciones de base de datos
│   ├── models.py            # Modelos de datos
│   ├── forms.py             # Formularios (ObraForm)
│   ├── views.py             # Vistas (lista_obras, crear_obra)
│   ├── urls.py              # Rutas de la aplicación
│   ├── admin.py             # Configuración del admin
│   └── tests.py             # Tests
├── teatro_proyecto/         # Configuración del proyecto
│   ├── settings.py          # Configuración
│   ├── urls.py              # Rutas principales
│   ├── wsgi.py              # WSGI
│   └── asgi.py              # ASGI
├── templates/               # Templates HTML
│   └── teatro/
│       ├── lista_obras.html
│       └── crear_obra.html
├── manage.py                # Gestor de Django
├── db.sqlite3               # Base de datos
└── requirements.txt         # Dependencias
```

## Funcionalidades

- Listar obras de teatro
- Crear nuevas obras desde la aplicación
- Panel de administración Django

