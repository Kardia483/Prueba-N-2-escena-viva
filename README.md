# Escena Viva — Cartelera Cultural de Santiago

Proyecto Django para la evaluación de Semanas 3-5 (Programación Back End,
INACAP): templates reutilizables y urls, modelos + ORM + migraciones +
Django Admin, y CRUD con ModelForm + vistas genéricas + seguridad.

## Cómo correrlo

```
python -m venv venv
venv\Scripts\activate          (Windows)   /   source venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego entra a `http://127.0.0.1:8000/`.

- `/admin/` → panel de administración (con el usuario del paso anterior).
- `/accounts/login/` → iniciar sesión (necesario para crear/editar/borrar
  eventos). El link "Iniciar sesión" de la navbar ya apunta ahí.
- Crea primero una o dos **Categorías** desde `/admin/` (ej: Teatro,
  Música, Cine, Exposiciones) antes de crear eventos, porque cada evento
  necesita una categoría.

## Mapa del proyecto → requisitos de la pauta

| Requisito de la pauta | Dónde está |
|---|---|
| Estructura en 2 niveles + `include()` | `escena_viva/urls.py` incluye `eventos/urls.py` |
| Modelo de clasificación + modelo principal con FK | `eventos/models.py` → `Categoria` y `Evento` (`Evento.categoria` es FK) |
| Migraciones | `eventos/migrations/0001_initial.py` |
| Django Admin con `list_display` + filtros/búsqueda | `eventos/admin.py` |
| `ModelForm` | `eventos/forms.py` → `EventoForm` |
| CRUD completo (listar, ver, crear, editar, borrar) | `eventos/views.py` → `EventoListView`, `EventoDetailView`, `EventoCreateView`, `EventoUpdateView`, `EventoDeleteView` (vistas genéricas) |
| Seguridad: login/logout, `LoginRequiredMixin`, `csrf_token` | login/logout vienen de `django.contrib.auth.urls` (incluido en `escena_viva/urls.py`); `LoginRequiredMixin` en Create/Update/Delete; `{% csrf_token %}` en todos los `<form method="post">` |
| `base.html` con `{% extends %}` / `{% block %}` | `eventos/templates/base.html`; todas las demás páginas lo extienden |
| Header/navbar/footer una sola vez | dentro de `base.html` (nunca se repiten en otro archivo) |
| Página con datos desde JSON | `eventos/data/clima.json` + vista `clima()` en `views.py` (usa `open()` + `json.load()`) + `eventos/templates/eventos/clima.html` |
| Filtrado por categoría con el ORM | `EventosPorCategoriaView` en `views.py`: `Evento.objects.filter(categoria=...)` |

## Conceptos clave para repasar antes del cuestionario

Como el cuestionario te va a mostrar tu propio código con partes borradas,
vale la pena que entiendas bien estas ideas (no solo que el código
funcione):

1. **ForeignKey**: `Evento.categoria` guarda el `id` de una `Categoria`.
   `on_delete=models.CASCADE` significa que si borras una categoría, se
   borran también sus eventos. `related_name="eventos"` permite hacer
   `categoria.eventos.all()` desde el lado de `Categoria`.

2. **Vistas genéricas (CBV)**: en vez de escribir a mano
   `if request.method == "POST":`, las clases `ListView`, `DetailView`,
   `CreateView`, `UpdateView`, `DeleteView` ya traen esa lógica. Por
   ejemplo, `CreateView` sabe mostrar el formulario vacío en GET y
   guardarlo en POST si es válido, usando el `form_class` que le indiques.

3. **`LoginRequiredMixin`**: se pone como la PRIMERA clase heredada
   (`class EventoCreateView(LoginRequiredMixin, CreateView):`). Si el
   usuario no inició sesión, lo redirige automáticamente a `LOGIN_URL`
   (configurado en `settings.py` como `"login"`).

4. **`ModelForm`**: `EventoForm` no define los campos a mano, los toma
   del modelo `Evento` a través de `class Meta: model = Evento; fields = [...]`.
   Esto evita repetir las validaciones que ya tiene el modelo.

5. **`get_queryset()` vs `queryset =`**: se usa `get_queryset()` como
   método (no un atributo fijo) cuando el filtro depende de algo que
   cambia en cada request, como el `pk` de la categoría en la URL
   (`self.kwargs["pk"]`).

6. **`{% csrf_token %}`**: Django exige este token oculto en todo
   formulario que use `method="post"`, para evitar que otro sitio web
   envíe formularios en tu nombre sin que te des cuenta.

7. **`json.load()`**: la vista `clima()` abre el archivo
   `eventos/data/clima.json` con `open(..., encoding="utf-8")` y lo
   convierte de texto a un diccionario de Python con `json.load(archivo)`,
   que luego se recorre en el template con `{% for dia in pronostico %}`.

8. **Context processor** (`eventos/context_processors.py`): es una
   función que Django ejecuta automáticamente en CADA request y agrega su
   resultado al contexto de CUALQUIER template, sin que cada vista tenga
   que pasarlo a mano. Por eso `base.html` puede hacer
   `{% for cat in categorias_nav %}` aunque ninguna vista se lo pase
   directamente — está registrado en `TEMPLATES` dentro de `settings.py`.
