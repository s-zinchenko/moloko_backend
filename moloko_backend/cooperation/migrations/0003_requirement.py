# Generated by Django 4.0.6 on 2023-01-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0002_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Требование к поставщикам и производителям')),
            ],
            options={
                'verbose_name': 'Требование к поставщикам и производителям',
                'verbose_name_plural': 'Требования к поставщикам и производителям',
            },
        ),
    ]
