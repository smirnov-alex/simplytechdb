# Generated by Django 3.0 on 2021-08-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techdb', '0005_siteequipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteequipment',
            name='device',
            field=models.TextField(blank=True, null=True, verbose_name='Оборудование'),
        ),
        migrations.AlterField(
            model_name='siteequipment',
            name='serial_number',
            field=models.TextField(blank=True, null=True, verbose_name='Серийный номер'),
        ),
    ]