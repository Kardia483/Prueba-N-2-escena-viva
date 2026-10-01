"""
urls.py de la APP (nivel 2 de las "dos niveles" que pide la pauta). Cada
ruta tiene su name= para poder usar {% url 'nombre' %} en los templates.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventoListView.as_view(), name="evento_list"),
    path("evento/nuevo/", views.EventoCreateView.as_view(), name="evento_create"),
    path("evento/<int:pk>/", views.EventoDetailView.as_view(), name="evento_detail"),
    path("evento/<int:pk>/editar/", views.EventoUpdateView.as_view(), name="evento_update"),
    path("evento/<int:pk>/borrar/", views.EventoDeleteView.as_view(), name="evento_delete"),
    path("categoria/<int:pk>/", views.EventosPorCategoriaView.as_view(), name="categoria_detail"),
    path("clima/", views.clima, name="clima"),
]
