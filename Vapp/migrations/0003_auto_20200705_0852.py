# Generated by Django 3.0.8 on 2020-07-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vapp', '0002_auto_20200705_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='freight_by_customer',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='freight_by_owner',
            field=models.FloatField(default=0),
        ),
    ]
