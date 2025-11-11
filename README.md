# Entrega3
# Teatro Proyecto

Aplicación Django para gestionar obras de teatro.

## Datos personales

-Nombre: Juan Pablo Petean
-Curso: Programación en Python
-Tema: Entrega 3: Página web de obra de teatro

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

En Windows:
```bash
venv\Scripts\activate
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

## Estructura del Proyecto

```
teatro_proyecto/
├── teatro/                  # Aplicación principal
│   ├── migrations/         # Migraciones de base de datos
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas
│   ├── urls.py            # Rutas de la aplicación
│   ├── admin.py           # Configuración del admin
│   └── tests.py           # Tests
├── teatro_proyecto/        # Configuración del proyecto
│   ├── settings.py        # Configuración
│   ├── urls.py            # Rutas principales
│   ├── wsgi.py            # WSGI
│   └── asgi.py            # ASGI
├── templates/             # Templates HTML
│   └── teatro/
│       └── lista_obras.html
├── manage.py              # Gestor de Django
├── db.sqlite3             # Base de datos
└── requirements.txt       # Dependencias
```

## Funcionalidades

- Listar obras de teatro
- Panel de administración Django

