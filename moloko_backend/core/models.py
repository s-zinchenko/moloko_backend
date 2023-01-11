# type: ignore
from typing import Dict

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, email: str, password: str, **extra_fields: Dict
    ) -> AbstractBaseUser:
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email: str = None, password: str = None, **extra_fields
    ) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self, email: str, password: str, **extra_fields
    ) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    email = models.EmailField("E-mail", unique=True)
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log " 
            "into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def get_short_name(self):
        return self.email


class Company(SingletonModel):
    class Meta:
        verbose_name = "Компания"

    name = models.CharField(max_length=255, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание")
    map_image = models.FileField(verbose_name="Изображение карты")

    def __str__(self) -> str:
        return "Компания"


class Fact(models.Model):
    class Meta:
        verbose_name = "Факт"
        verbose_name_plural = "Факты"

    number = models.SmallIntegerField(verbose_name="Число")
    title = models.CharField(max_length=256, verbose_name="Описание")
    company = models.ForeignKey("core.Company", on_delete=models.CASCADE, verbose_name="Факт о компании")

    def __str__(self) -> str:
        return f"Факт о {self.company.name}"


class Management(models.Model):
    class Meta:
        verbose_name = "Управляющий"
        verbose_name_plural = "Управляющие"

    first_name = models.CharField(max_length=512, verbose_name="Имя")
    last_name = models.CharField(max_length=512, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=512, verbose_name="Отчество")
    role = models.CharField(max_length=512, verbose_name="Должность")
    portrait = models.FileField(verbose_name="Портрет")

    @property
    def name(self) -> str:
        return f"{self.last_name} {self.first_name[0]}.{self.middle_name[0]}."

    def __str__(self) -> str:
        return self.name
