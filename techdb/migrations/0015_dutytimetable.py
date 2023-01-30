# Generated by Django 3.1.13 on 2022-10-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techdb', '0014_dutyshedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='DutyTimetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала дежурства')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания дежурства')),
                ('duty', models.TextField(blank=True, null=True, verbose_name='Дежурный')),
                ('duty_add', models.TextField(blank=True, null=True, verbose_name='Группа дежурного')),
                ('support', models.TextField(blank=True, null=True, verbose_name='Поддержка')),
                ('support_add', models.TextField(blank=True, null=True, verbose_name='Группа поддержки')),
            ],
            options={
                'verbose_name': 'дежурный',
                'verbose_name_plural': 'Дежурные',
                'ordering': ['date_start'],
            },
        ),
    ]
