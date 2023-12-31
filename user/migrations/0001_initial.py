# Generated by Django 5.0 on 2023-12-20 07:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "username",
                    models.CharField(
                        max_length=150,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_username",
                                message="Enter a valid username. This value may contain only letters, digits, and @/./+/-/_ characters.",
                                regex="^[\\w.@+-]+$",
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
