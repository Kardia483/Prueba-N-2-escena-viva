import json
from pathlib import Path

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import EventoForm
from .models import Categoria, Evento


class EventoListView(ListView):
    """Portada: los próximos eventos publicados, destacados primero."""

    model = Evento
    template_name = "eventos/evento_list.html"
    context_object_name = "eventos"

    def get_queryset(self):
        return Evento.objects.filter(publicado=True).order_by("-destacado", "fecha")


class EventosPorCategoriaView(ListView):
    """Lista los eventos de UNA categoría (filtro hecho con el ORM)."""

    model = Evento
    template_name = "eventos/categoria.html"
    context_object_name = "eventos"

    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, pk=self.kwargs["pk"])
        return Evento.objects.filter(categoria=self.categoria, publicado=True).order_by("fecha")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = self.categoria
        return context


class EventoDetailView(DetailView):
    model = Evento
    template_name = "eventos/evento_detail.html"
    context_object_name = "evento"


class EventoCreateView(LoginRequiredMixin, CreateView):
    """Crear evento: solo con sesión iniciada (LoginRequiredMixin)."""

    model = Evento
    form_class = EventoForm
    template_name = "eventos/evento_form.html"

    def get_success_url(self):
        return reverse_lazy("evento_detail", kwargs={"pk": self.object.pk})


class EventoUpdateView(LoginRequiredMixin, UpdateView):
    """Editar evento: solo con sesión iniciada."""

    model = Evento
    form_class = EventoForm
    template_name = "eventos/evento_form.html"

    def get_success_url(self):
        return reverse_lazy("evento_detail", kwargs={"pk": self.object.pk})


class EventoDeleteView(LoginRequiredMixin, DeleteView):
    """Borrar evento (con página de confirmación): solo con sesión iniciada."""

    model = Evento
    template_name = "eventos/evento_confirm_delete.html"
    success_url = reverse_lazy("evento_list")


def clima(request):
    """
    Página extra que lee datos desde un archivo JSON (no desde la base de
    datos) usando open() + json.load(), y los muestra con {% for %}.
    """
    ruta = Path(settings.BASE_DIR) / "eventos" / "data" / "clima.json"
    with open(ruta, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    contexto = {
        "ciudad": datos.get("ciudad", "Santiago"),
        "pronostico": datos.get("pronostico", []),
    }
    return render(request, "eventos/clima.html", contexto)
