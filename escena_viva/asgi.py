"""Configuración ASGI para el proyecto escena_viva."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "escena_viva.settings")

application = get_asgi_application()
