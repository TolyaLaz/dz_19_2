# Generated by Django 5.0.6 on 2024-07-10 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Введите описание продукта",
                        max_length=200,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        help_text="Введите категорию продукта",
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "name",
                    models.CharField(
                        help_text="Введите наименование продукта",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Введите описание продукта",
                        max_length=200,
                        null=True,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="catalog/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Укажите цену продукта",
                        verbose_name="Цена за покупку",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Укажите дату последнего изменения",
                        null=True,
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию продукта",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="categories",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "price"],
            },
        ),
    ]
