# Generated by Django 4.0.6 on 2023-01-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.FileField(default=None, upload_to='', verbose_name='Иконка категории'),
        ),
    ]
