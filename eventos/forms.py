from django import forms

from .models import Evento


class EventoForm(forms.ModelForm):
    """
    ModelForm del modelo principal (Evento), usado tanto para crear como
    para editar. Se declara `fecha` aparte para que el input sea un
    selector de fecha y hora nativo del navegador (datetime-local).
    """

    fecha = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
        help_text="Fecha y hora del evento",
    )

    class Meta:
        model = Evento
        fields = [
            "titulo",
            "categoria",
            "descripcion",
            "fecha",
            "lugar",
            "precio",
            "imagen",
            "destacado",
            "publicado",
        ]
