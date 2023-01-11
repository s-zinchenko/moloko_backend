import os
from email.policy import default

import environ
from django.db.models import BigAutoField, FileField as DbFileField
from django.forms import FileField as FormFileField, ChoiceField
from marshmallow import fields

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

VERSION = "0.0.1"
env = environ.Env()
environ.Env.read_env(env.str("ENV_PATH", ".env"))

SECRET_KEY = env.str("SECRET_KEY", default="my-secret-key")
DEBUG = env.bool("DEBUG", default=False)
SILK = env.bool("SILK", default=True)

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [env.str("CSRF_TRUSTED_ORIGINS", default="https://*.ktsdev.ru")]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "solo",
    "import_export",
]

PROJECT_APPS = [
    "moloko_backend.core",
    "moloko_backend.news",
    "moloko_backend.cooperation",
    "moloko_backend.bids",
]

INSTALLED_APPS += PROJECT_APPS

if SILK:
    INSTALLED_APPS += ["silk"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if SILK:
    MIDDLEWARE = ["silk.middleware.SilkyMiddleware"] + MIDDLEWARE

ROOT_URLCONF = "moloko_backend.application.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = (
    "moloko_backend.application.wsgi.application"
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DATABASE_NAME", default=""),
        "USER": env.str("DATABASE_USER", default=""),
        "PASSWORD": env.str("DATABASE_PASSWORD", default=""),
        "HOST": env.str("DATABASE_HOST", default="127.0.0.1"),
        "PORT": env.int("DATABASE_PORT", default="5432"),
        "TEST": {"CHARSET": "UTF8", "TEMPLATE": "template0"},
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

AUTH_USER_MODEL = "core.User"

LANGUAGE_CODE = "ru-RU"
TIME_ZONE = "Europe/Moscow"



USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/dj_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

if not DEBUG:
    if env.bool("LOGGING_PATH", default=False):
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "verbose": {
                    "format": "LEVEL:%(levelname)s "
                    "TIME:%(asctime)s MESSAGE:%(message)s"
                },
            },
            "handlers": {
                "file": {
                    "level": "INFO",
                    "class": "logging.FileHandler",
                    "filename": env.str("LOGGING_PATH"),
                    "formatter": "verbose",
                }
            },
            "loggers": {
                "django": {
                    "handlers": ["file"],
                    "level": "INFO",
                    "propagate": True,
                }
            },
        }

SERIALIZER_FIELD_MAPPING = {
    BigAutoField: fields.Int,
    DbFileField: fields.Str,
}
SERIALIZER_FORM_FIELD_MAPPING = {
    FormFileField: fields.Str,
    ChoiceField: fields.Str
}
