import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=80, unique=True)),
            ],
            options={
                "verbose_name": "Categoría",
                "verbose_name_plural": "Categorías",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=150)),
                ("descripcion", models.TextField(blank=True)),
                (
                    "fecha",
                    models.DateTimeField(help_text="Fecha y hora en que ocurre el evento"),
                ),
                ("lugar", models.CharField(max_length=150)),
                (
                    "precio",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Precio de la entrada en pesos chilenos. Déjalo en 0 si es gratis.",
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="eventos/"),
                ),
                (
                    "destacado",
                    models.BooleanField(
                        default=False,
                        help_text="Los eventos destacados aparecen primero en la portada.",
                    ),
                ),
                (
                    "publicado",
                    models.BooleanField(
                        default=True,
                        help_text="Solo los eventos publicados se muestran en el sitio.",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eventos",
                        to="eventos.categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Evento",
                "verbose_name_plural": "Eventos",
                "ordering": ["fecha"],
            },
        ),
    ]
