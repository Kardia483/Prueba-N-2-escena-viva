from django.contrib import admin

from .models import Categoria, Evento


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha", "lugar", "precio", "destacado", "publicado")
    list_filter = ("categoria", "destacado", "publicado")
    search_fields = ("titulo", "lugar")
