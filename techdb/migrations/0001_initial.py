# Generated by Django 3.0 on 2021-08-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Сайт')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('status', models.TextField(blank=True, null=True, verbose_name='Статус')),
                ('alternative', models.TextField(blank=True, null=True, verbose_name='Альтернатива')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты',
                'ordering': ['title'],
            },
        ),
    ]
