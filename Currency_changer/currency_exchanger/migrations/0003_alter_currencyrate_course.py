# Generated by Django 4.1.7 on 2023-05-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchanger', '0002_currencyrate_remove_currency_currency_currency_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyrate',
            name='course',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
