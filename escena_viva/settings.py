"""
Configuración de Django para el proyecto escena_viva.

Escena Viva — Cartelera Cultural de Santiago. Evaluación Semanas 3-5 de
Programación Back End (INACAP): templates reutilizables y urls, modelos +
ORM + Admin, y CRUD con ModelForm + vistas genéricas + seguridad.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: clave solo para desarrollo/evaluación local.
SECRET_KEY = "django-insecure-escena-viva-clave-de-desarrollo-cambia-esto"

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # App propia de Escena Viva
    "eventos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "escena_viva.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Context processor propio: agrega la lista de categorías
                # a TODOS los templates, para que la navbar siempre pueda
                # mostrarlas sin que cada vista tenga que pasarlas a mano.
                "eventos.context_processors.categorias",
            ],
        },
    },
]

WSGI_APPLICATION = "escena_viva.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "es"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"

# Archivos de media (imágenes de los eventos)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Autenticación: a dónde mandar en cada caso.
# "django.contrib.auth.urls" (incluido en escena_viva/urls.py bajo
# accounts/) ya trae la vista de login con name="login", por eso
# LOGIN_URL apunta a ese nombre.
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "evento_list"
LOGOUT_REDIRECT_URL = "evento_list"
