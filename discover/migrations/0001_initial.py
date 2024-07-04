# Generated by Django 4.2.13 on 2024-06-21 08:32

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "featured_image",
                    cloudinary.models.CloudinaryField(
                        default="placeholder", max_length=255, verbose_name="image"
                    ),
                ),
                ("content", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("excerpt", models.TextField(blank=True)),
                ("budget", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("EUR", "Euro"),
                            ("CHF", "Swiss Franc"),
                            ("GBP", "Pound Sterling"),
                        ],
                        default="EUR",
                        max_length=3,
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("nights", models.IntegerField(blank=True, null=True)),
                ("people", models.IntegerField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
