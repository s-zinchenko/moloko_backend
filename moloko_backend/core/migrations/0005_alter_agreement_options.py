# Generated by Django 4.0.6 on 2023-01-25 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_agreement_delete_management'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreement',
            options={'verbose_name': 'Согласие на обработку персональных данных'},
        ),
    ]
