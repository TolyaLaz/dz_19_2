# Generated by Django 5.1 on 2024-08-21 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]