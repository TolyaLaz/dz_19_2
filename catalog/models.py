from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=200,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name='categories',
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Укажите цену продукта"
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"{self.name} {self.price}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.CharField(
        max_length=200, verbose_name="Описание", help_text="Введите описание продукта"
    )


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
