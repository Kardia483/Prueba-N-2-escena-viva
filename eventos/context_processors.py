"""
Context processor: agrega la lista de categorías a TODOS los templates
automáticamente (está registrado en settings.py, dentro de TEMPLATES).
Así la navbar de base.html puede mostrar los links de categorías sin que
cada vista tenga que acordarse de pasarlas en su contexto.
"""

from .models import Categoria


def categorias(request):
    return {"categorias_nav": Categoria.objects.all()}
