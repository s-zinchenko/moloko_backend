# Generated by Django 4.0.6 on 2023-01-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Файл согласия на обработку персональных данных')),
            ],
            options={
                'verbose_name': 'Компания',
            },
        ),
        migrations.DeleteModel(
            name='Management',
        ),
    ]
