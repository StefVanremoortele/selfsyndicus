# Generated by Django 5.1.5 on 2025-01-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buildings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Privatives",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
