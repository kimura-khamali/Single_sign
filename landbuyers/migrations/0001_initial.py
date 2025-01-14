# Generated by Django 5.1.1 on 2024-09-06 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("lawyers", "__first__"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LandBuyer",
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
                ("address", models.CharField(max_length=30)),
                (
                    "lawyer",
                    models.ForeignKey(
                        blank=True,
                        default="some_default_lawyer",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lawyers.lawyer",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
