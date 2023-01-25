from typing import Dict

from django.db import models

from moloko_backend.bids.mixins import SendEmailMixin


class LogisticBid(SendEmailMixin, models.Model):
    class Meta:
        verbose_name = "Логистическая заявка"
        verbose_name_plural = "Логистические заявки"

    email_recipient = ""

    full_name = models.CharField(max_length=512, verbose_name="Полное имя")
    departure_address = models.CharField(
        max_length=512, verbose_name="Адрес отправления"
    )
    contact_phone = models.CharField(
        max_length=32, verbose_name="Контактный телефон"
    )
    cargo_weight = models.PositiveIntegerField(verbose_name="Вес груза в КГ")
    email = models.EmailField(verbose_name="Электронная почта")
    cargo_descriptions = models.TextField(verbose_name="Описание груза")

    def __str__(self) -> str:
        return f"{self.full_name} {self.contact_phone}"


class CooperationBid(SendEmailMixin, models.Model):
    class Meta:
        verbose_name = "Заявка на сотрудничество"
        verbose_name_plural = "Заявки на сотрудничество"

    email_subject: str = "Заявка на сотрудничество"
    # email_recipient = "moloko.optom@mail.ru"
    email_recipient = "zinchieko02@mail.ru"

    full_name = models.CharField(max_length=512, verbose_name="Полное имя")
    contact_phone = models.CharField(
        max_length=32, verbose_name="Контактный телефон"
    )
    email = models.EmailField(verbose_name="Электронная почта")
    company_name = models.CharField(
        max_length=512, verbose_name="Название компании"
    )
    document = models.FileField(verbose_name="Документ")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self) -> str:
        return f"{self.full_name} {self.contact_phone}"

    @property
    def to_dict(self) -> Dict[str, str]:
        return {
            "Полное имя": self.full_name,
            "Контактный телефон": self.contact_phone,
            "Электронная почта": self.email,
            "Компания": self.company_name,
            "Комментарий": self.comment,
            "Документ": self.document,
        }


class PriceListBid(SendEmailMixin, models.Model):
    class Meta:
        verbose_name = "Заявка на прайс-лист"
        verbose_name_plural = "Заявки на прайс-листы"

    email_subject: str = "Заявка на прайс-лист"
    # email_recipient = "moloko.optom@mail.ru"
    email_recipient = "zinchieko02@mail.ru"

    name = models.CharField(max_length=512, verbose_name="Имя")
    contact_phone = models.CharField(
        max_length=32, verbose_name="Контактный телефон"
    )
    email = models.EmailField(verbose_name="Электронная почта")
    company_name = models.CharField(
        max_length=512, verbose_name="Название компании"
    )

    def __str__(self) -> str:
        return f"{self.name} {self.contact_phone}"

    @property
    def to_dict(self) -> Dict[str, str]:
        return {
            "Контактный телефон": self.contact_phone,
            "Электронная почта": self.email,
            "Компания": self.company_name,
            "Имя": self.name,
        }
