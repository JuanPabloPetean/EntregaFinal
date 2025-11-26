# Entrega Final — Teatro Proyecto 🎭

Aplicación Django completa para gestionar obras de teatro con autenticación de usuarios, CRUD completo y herencia de templates.

## Datos personales

- **Nombre:** Juan Pablo Petean
- **Curso:** Programación en Python
- **Tema:** Entrega Final: Página Web de Gestión de Obras de Teatro

## Requisitos

- Python 3.13+
- Django 5.2.8
- Pillow 10.0.0 (para manejo de imágenes)

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/JuanPabloPetean/Entrega3.git
cd teatro_proyecto
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear superusuario (admin)
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

El servidor estará disponible en:
- **Aplicación:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

## Características Implementadas ✅

### 1. Sistema de Autenticación
- ✅ Registro de usuarios (username, email, password)
- ✅ Login / Logout
- ✅ Vistas protegidas con `LoginRequiredMixin` y `@login_required`

### 2. Gestión de Obras (CRUD)
- ✅ **Listar** obras de teatro
- ✅ **Ver detalle** de cada obra
- ✅ **Crear** nueva obra (solo usuarios autenticados)
- ✅ **Editar** obra (solo usuarios autenticados)
- ✅ **Eliminar** obra (solo usuarios autenticados)
- ✅ Soporte para imágenes/archivos

### 3. Vistas Basadas en Clases (CBV)
- ✅ `ObraListView` (ListView)
- ✅ `ObraDetailView` (DetailView)
- ✅ `ObraCreateView` (CreateView con LoginRequiredMixin)
- ✅ `ObraUpdateView` (UpdateView con LoginRequiredMixin)
- ✅ `ObraDeleteView` (DeleteView con LoginRequiredMixin)
- ✅ `RegisterView` (CreateView para registro)

### 4. Herencia de Templates
- ✅ `base.html` con estructura base, navegación y footer
- ✅ Todas las plantillas heredan de `base.html`
- ✅ Bloques reutilizables: `title`, `content`, `extra_css`

### 5. Modelo Principal
- ✅ Modelo `Obra` con campos:
  - `titulo` (CharField, 100)
  - `autor` (CharField, 100)
  - `descripcion` (TextField)
  - `fecha_estreno` (DateField)
  - `genero` (CharField, 50)
  - `imagen` (FileField, opcional)

### 6. Vistas Especiales
- ✅ Vista **Home** (`/`) con bienvenida
- ✅ Vista **Acerca de** (`/about/`) con información personal
- ✅ Vista **Login** (`/users/login/`)
- ✅ Vista **Registro** (`/users/register/`)
- ✅ Vista **Logout**

### 7. Mensajes y UX
- ✅ Mensajes de éxito al crear, editar, eliminar
- ✅ Mensajes de no hay datos cuando la lista está vacía
- ✅ Interfaz responsive y amigable

## Estructura del Proyecto

```
teatro_proyecto/
├── teatro/                      # App principal
│   ├── migrations/              # Migraciones de BD
│   ├── models.py                # Modelo Obra
│   ├── forms.py                 # ObraForm (ModelForm)
│   ├── views.py                 # Vistas (CBV y FBV)
│   ├── urls.py                  # Rutas de la app
│   ├── admin.py                 # Configuración admin
│   └── tests.py
├── users/                       # App de autenticación
│   ├── migrations/
│   ├── forms.py                 # RegisterForm
│   ├── views.py                 # Login, Logout, Register
│   ├── urls.py                  # Rutas de users
│   └── admin.py
├── teatro_proyecto/             # Configuración del proyecto
│   ├── settings.py              # Configuración (INSTALLED_APPS, MEDIA, etc.)
│   ├── urls.py                  # URLs principales
│   ├── wsgi.py
│   └── asgi.py
├── templates/                   # Templates
│   ├── base.html                # Template base (herencia)
│   ├── teatro/
│   │   ├── home.html            # Home
│   │   ├── about.html           # Acerca de
│   │   ├── lista_obras.html     # Listado de obras
│   │   ├── obra_detail.html     # Detalle de obra
│   │   ├── crear_obra.html      # Crear obra
│   │   ├── editar_obra.html     # Editar obra
│   │   └── eliminar_obra.html   # Confirmar eliminación
│   └── users/
│       ├── login.html           # Login
│       └── register.html        # Registro
├── media/                       # Archivos subidos (gitignored)
├── manage.py
├── db.sqlite3                   # BD (gitignored)
├── requirements.txt             # Dependencias
├── .gitignore
└── README.md
```

## Flujos de Trabajo

### Flujo de Usuario No Autenticado
1. Accede a Home (`/`)
2. Ve todas las obras en `/obras/`
3. Puede ver detalles de cada obra
4. Intenta crear → redirigido a login
5. Se registra o inicia sesión en `/users/register/` o `/users/login/`

### Flujo de Usuario Autenticado
1. Accede a Home (`/`)
2. Ve todas las obras + botones de crear/editar/eliminar
3. Crea obra nueva → `/obras/crear/` + redirige a listado
4. Edita obra → `/obras/<id>/editar/`
5. Elimina obra → `/obras/<id>/eliminar/` + confirmación
6. Cierra sesión → `/users/logout/`

## URLs del Proyecto

```
/                           → Home
/about/                     → Acerca de
/obras/                     → Lista de obras (ListView)
/obras/<id>/                → Detalle de obra (DetailView)
/obras/crear/               → Crear obra (CreateView, requiere login)
/obras/<id>/editar/         → Editar obra (UpdateView, requiere login)
/obras/<id>/eliminar/       → Eliminar obra (DeleteView, requiere login)
/users/login/               → Login
/users/logout/              → Logout
/users/register/            → Registro
/admin/                     → Admin panel
```

## Requisitos Técnicos Cumplidos

✅ Entrega individual subida a GitHub
✅ README como entrega final (este archivo)
✅ `.gitignore` con venv, __pycache__, db.sqlite3, media
✅ `requirements.txt` actualizado
✅ Herencia de templates (base.html)
✅ Mínimo 2 CBV (6 implementadas)
✅ Mínimo 1 Mixin en CBV (LoginRequiredMixin)
✅ Mínimo 1 decorador en FBV (@login_required)
✅ Vista de inicio (Home)
✅ Vista "Acerca de mi"
✅ Modelo principal con 3+ CharFields y 1 FileField
✅ Vista de listado con datos parciales
✅ Acceso a detalle, crear, editar, eliminar desde listado
✅ Registrados todos los modelos en admin
✅ App separada para usuarios/autenticación
✅ Vistas para login, logout, registro
✅ Campos requeridos: username, email, password

## Dependencias

Ver `requirements.txt`:
```
Django==5.2.8
Pillow==10.0.0
setuptools==80.9.0
asgiref==3.10.0
sqlparse==0.5.3
tzdata==2025.2
```

## Notas Importantes

1. **Base de datos:** No incluida en el repo (gitignored). Se crea automáticamente con `python manage.py migrate`.
2. **Imágenes:** Se cargan en la carpeta `media/` (gitignored). Las imágenes estáticas van en `static/`.
3. **Seguridad:** Debug está en True para desarrollo. En producción, cambiar a False y configurar SECRET_KEY.
4. **Admin:** Usa la app por defecto de Django. Accede con el superusuario creado.

## Problemas Comunes

**Error: "Cannot use ImageField because Pillow is not installed"**
→ Ejecuta: `pip install Pillow`

**Error: "No such table: teatro_obra"**
→ Ejecuta: `python manage.py migrate`

**Página no carga imágenes**
→ Verifica que `DEBUG = True` en settings.py y que las URLs de media estén configuradas.

## Autor

**Juan Pablo Petean** - Curso de Programación en Python

---

**Última actualización:** Noviembre 2025

