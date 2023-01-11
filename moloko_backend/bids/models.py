from django.db import models


class LogisticBid(models.Model):
    class Meta:
        verbose_name = "Логистическая заявка"
        verbose_name_plural = "Логистические заявки"

    full_name = models.CharField(max_length=512, verbose_name="Полное имя")
    departure_address = models.CharField(max_length=512, verbose_name="Адрес отправления")
    contact_phone = models.CharField(max_length=32, verbose_name="Контактный телефон")
    cargo_weight = models.PositiveIntegerField(verbose_name="Вес груза в КГ")
    email = models.EmailField(verbose_name="Электронная почта")
    cargo_descriptions = models.TextField(verbose_name="Описание груза")

    def __str__(self) -> str:
        return f"{self.full_name} {self.contact_phone}"


class CooperationBid(models.Model):
    class Meta:
        verbose_name = "Заявка на сотрудничество"
        verbose_name_plural = "Заявки на сотрудничество"

    full_name = models.CharField(max_length=512, verbose_name="Полное имя")
    contact_phone = models.CharField(max_length=32, verbose_name="Контактный телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    company_name = models.CharField(max_length=512, verbose_name="Название компании")
    document = models.FileField(verbose_name="Документ")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self) -> str:
        return f"{self.full_name} {self.contact_phone}"
