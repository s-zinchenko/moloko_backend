from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    title = models.CharField(max_length=512, verbose_name="Название категории")

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    title = models.CharField(max_length=512, verbose_name="Название товара")
    category = models.ForeignKey("goods.Category", on_delete=models.CASCADE, verbose_name="Категория товара")

    def __str__(self) -> str:
        return self.title
