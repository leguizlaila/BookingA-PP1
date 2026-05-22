# Plataforma de Reservas de Alojamientos

Plataforma web tipo Airbnb desarrollada con **Django** y **PostgreSQL**, que permite a usuarios publicar alojamientos, realizar reservas, gestionar pagos y dejar reseñas.

## Tecnologías utilizadas
- **Backend:** Python 3.11 / Django 5.x
- **Base de datos:** PostgreSQL 15
- **Variables de entorno:** python-decouple
- **CI/CD:** GitHub Actions

##  Estructura del proyecto

```
proyecto/
├── config/                  # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── reservas/                # App principal
│   ├── models.py            # Modelos: Usuario, Alojamiento, Reserva, etc.
│   ├── admin.py             # Registro en Django Admin
│   └── migrations/          # Migraciones generadas
├── seed.py                  # Script de datos semilla
├── requirements.txt
├── .env.example             # Plantilla de variables de entorno
├── .github/
│   └── workflows/
│       └── django-ci.yml    # GitHub Actions CI
└── README.md
```

## Instalación local paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus datos reales de PostgreSQL
```

### 5. Crear la base de datos en PostgreSQL

```sql
CREATE DATABASE airbnb_db;
```

### 6. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear superusuario para el Admin

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el script de datos semilla

```bash
python seed.py
```

### 9. Correr el servidor de desarrollo

```bash
python manage.py runserver
```

Accedé al admin en: [http://localhost:8000/admin](http://localhost:8000/admin)

## Variables de entorno requeridas

| Variable       | Descripción                          | Ejemplo               |
|----------------|--------------------------------------|-----------------------|
| `SECRET_KEY`   | Clave secreta de Django              | `django-insecure-...` |
| `DEBUG`        | Modo debug                           | `True`                |
| `ALLOWED_HOSTS`| Hosts permitidos (separados por `,`) | `localhost`           |
| `DB_NAME`      | Nombre de la base de datos           | `airbnb_db`           |
| `DB_USER`      | Usuario de PostgreSQL                | `postgres`            |
| `DB_PASSWORD`  | Contraseña de PostgreSQL             | `tu_password`         |
| `DB_HOST`      | Host de la base de datos             | `localhost`           |
| `DB_PORT`      | Puerto de PostgreSQL                 | `5432`                |

##  Modelos del sistema

| Modelo               | Descripción                                      |
|----------------------|--------------------------------------------------|
| `Usuario`            | Usuarios del sistema (huéspedes y anfitriones)   |
| `Alojamiento`        | Propiedades publicadas por anfitriones           |
| `ImagenAlojamiento`  | Imágenes asociadas a cada alojamiento            |
| `Reserva`            | Reservas de huéspedes en alojamientos            |
| `Pago`               | Pagos asociados a reservas                       |
| `Resena`             | Reseñas y calificaciones de alojamientos         |

##  GitHub Actions

El workflow en `.github/workflows/django-ci.yml` se ejecuta automáticamente en cada `push` o `Pull Request` a `main`/`master`, y verifica que el proyecto no tenga errores de configuración con `python manage.py check`.

## Protección de ramas

El repositorio tiene configurada la protección de rama `main`:
-  No se permite push directo a `main`
- Todo cambio debe ingresar mediante Pull Request
-  Los cambios deben realizarse en la rama `nombre_apellido_parcial1`
