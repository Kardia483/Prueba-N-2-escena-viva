from django.db import models


class Categoria(models.Model):
    """
    Modelo de CLASIFICACIÓN: agrupa los eventos (Teatro, Música, Cine,
    Exposiciones...). Un evento pertenece a una sola categoría.
    """

    nombre = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    """
    Modelo PRINCIPAL de la cartelera. Cada evento pertenece a una
    Categoria mediante una ForeignKey (relación 1 categoría -> N eventos).
    """

    titulo = models.CharField(max_length=150)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="eventos",
    )
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(help_text="Fecha y hora en que ocurre el evento")
    lugar = models.CharField(max_length=150)
    precio = models.PositiveIntegerField(
        default=0,
        help_text="Precio de la entrada en pesos chilenos. Déjalo en 0 si es gratis.",
    )
    imagen = models.ImageField(upload_to="eventos/", blank=True, null=True)
    destacado = models.BooleanField(
        default=False, help_text="Los eventos destacados aparecen primero en la portada."
    )
    publicado = models.BooleanField(
        default=True, help_text="Solo los eventos publicados se muestran en el sitio."
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["fecha"]

    def __str__(self):
        return f"{self.titulo} ({self.categoria})"
