"""
urls.py del PROYECTO (nivel 1 de las "dos niveles" que pide la pauta).

Aquí solo se decide A QUÉ APP o sistema le toca cada prefijo de la URL:
- admin/      -> el Admin de Django
- accounts/   -> login/logout, ya hechos por Django (django.contrib.auth.urls)
- el resto    -> se delega por completo a eventos/urls.py con include()
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("eventos.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
