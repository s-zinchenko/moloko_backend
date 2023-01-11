from django.db import models


class TermOfCooperation(models.Model):
    class Meta:
        verbose_name = "Условие сотрудничества"
        verbose_name_plural = "Условия сотрудничества"

    class Type(models.TextChoices):
        COOPERATION = "cooperation"
        DELIVERY = "delivery"
        PAYMENT = "payment"

    type = models.CharField(max_length=16, choices=Type.choices, verbose_name="Тип условия")
    term = models.CharField(max_length=512, verbose_name="Условие")

    def __str__(self) -> str:
        return f"{self.type} {self.term}"


class Partner(models.Model):
    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"

    name = models.CharField(max_length=256, verbose_name="Имя партнёра")
    logo = models.FileField(verbose_name="Логотип партнёра")

    def __str__(self) -> str:
        return self.name


class Requirement(models.Model):
    class Meta:
        verbose_name = "Требование к поставщикам и производителям"
        verbose_name_plural = "Требования к поставщикам и производителям"

    title = models.CharField(max_length=512, verbose_name="Требование к поставщикам и производителям")

    def __str__(self) -> str:
        return self.title
