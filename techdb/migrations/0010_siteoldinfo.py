# Generated by Django 3.0 on 2021-09-12 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techdb', '0009_siteenergy'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteOldInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_info', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('title', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='techdb.Site', verbose_name='Сайт')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты_Старая_информация',
                'ordering': ['title'],
            },
        ),
    ]
