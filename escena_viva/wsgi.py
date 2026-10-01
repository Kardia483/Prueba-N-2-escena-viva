"""Configuración WSGI para el proyecto escena_viva."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "escena_viva.settings")

application = get_wsgi_application()
