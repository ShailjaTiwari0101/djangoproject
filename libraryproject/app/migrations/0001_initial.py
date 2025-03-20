# Generated by Django 5.1.7 on 2025-03-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "isbn",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=20)),
                ("author", models.CharField(max_length=20)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("programming", "programming"),
                            ("database", "database"),
                        ],
                        max_length=50,
                    ),
                ),
                ("price", models.FloatField()),
                ("qty", models.PositiveIntegerField(default=1)),
                ("dop", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
    ]
