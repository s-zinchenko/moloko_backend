from django.db import models


class News(models.Model):
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    title = models.CharField(max_length=512, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Основной текст")
    date = models.DateField(verbose_name="Дата")

    def __str__(self) -> str:
        return f"{self.title} {self.date}"
