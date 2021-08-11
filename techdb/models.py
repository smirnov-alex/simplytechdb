from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Наименование')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    def __str__(self):
        return self.name


class Site(models.Model):
    title = models.CharField(max_length=50, verbose_name='Сайт')
    category = models.ForeignKey('Category', null=True,
                                on_delete=models.PROTECT, verbose_name='Категория')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    status = models.TextField(null=True, blank=True, verbose_name='Статус')
    alternative = models.TextField(null=True, blank=True, verbose_name='Альтернатива')

    class Meta:
        verbose_name_plural = 'Сайты'
        verbose_name = 'Сайт'
        ordering = ['title']
