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
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    status = models.TextField(null=True, blank=True, verbose_name='Статус')
    alternative = models.TextField(null=True, blank=True, verbose_name='Альтернатива')

    class Meta:
        verbose_name_plural = 'Сайты'
        verbose_name = 'Сайт'
        ordering = ['title']

    def __str__(self):
        return self.title


class Comment(models.Model):
    site = models.ForeignKey(Site, related_name='comment', on_delete=models.PROTECT, verbose_name='Сайт')
    author = models.CharField(max_length=80, verbose_name='Автор')
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.text)


class SiteCommon(models.Model):
    title = models.OneToOneField(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    distance = models.IntegerField(null=True, blank=True, verbose_name='Расстояние')
    priority = models.TextField(null=True, blank=True, verbose_name='Приоритет')
    type_hardware = models.TextField(null=True, blank=True, verbose_name='Тип аппаратной')

    class Meta:
        verbose_name_plural = 'Сайты_общая'
        verbose_name = 'Сайт'
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class SiteBatteries(models.Model):
    title = models.OneToOneField(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    system_of_voltage = models.TextField(null=True, blank=True, verbose_name='Система питания')
    num_of_rect = models.IntegerField(null=True, blank=True, verbose_name='Количество выпрямителей')
    battery_type = models.TextField(null=True, blank=True, verbose_name='Тип АКБ')
    battery_num = models.IntegerField(null=True, blank=True, verbose_name='Количество АКБ')
    battery_cap = models.IntegerField(null=True, blank=True, verbose_name='Емкость АКБ')
    battery_date = models.DateField(null=True, blank=True, verbose_name='Дата установки АКБ')

    class Meta:
        verbose_name_plural = 'Сайты_АКБ'
        verbose_name = 'Сайт'
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class SiteEquipment(models.Model):
    title = models.ForeignKey(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    device = models.TextField(null=True, blank=True, verbose_name='Оборудование')
    serial_number = models.TextField(null=True, blank=True, verbose_name='Серийный номер')

    class Meta:
        verbose_name_plural = 'Сайты_оборудование'
        verbose_name = 'Сайт'
        ordering = ['device']

    def __str__(self):
        return str(self.title)


class SiteRRL(models.Model):
    title = models.ForeignKey(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    radiolink = models.TextField(null=True, blank=True, verbose_name='Направление РРЛ')
    type_rrl = models.TextField(null=True, blank=True, verbose_name='Тип оборудования')
    ip_access = models.TextField(null=True, blank=True, verbose_name='IP адрес')

    class Meta:
        verbose_name_plural = 'Сайты_РРЛ'
        verbose_name = 'Сайт'
        ordering = ['radiolink']

    def __str__(self):
        return str(self.title)


class SiteEnergy(models.Model):
    title = models.ForeignKey(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    energy = models.TextField(null=True, blank=True, verbose_name='Электропитание')

    class Meta:
        verbose_name_plural = 'Сайты_Электропитание'
        verbose_name = 'Сайт'
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class SiteOldInfo(models.Model):
    title = models.ForeignKey(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    old_info = models.TextField(null=True, blank=True, verbose_name='Информация')

    class Meta:
        verbose_name_plural = 'Сайты_Старая_информация'
        verbose_name = 'Сайт'
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class SiteQuazar(models.Model):
    title = models.ForeignKey(Site, on_delete=models.PROTECT, max_length=50, verbose_name='Сайт')
    location = models.TextField(null=True, blank=True, verbose_name='Локация')
    access = models.TextField(null=True, blank=True, verbose_name='Доступ')
    keys = models.TextField(null=True, blank=True, verbose_name='Ключи')
    energy = models.TextField(null=True, blank=True, verbose_name='Электроснабжение')
    other = models.TextField(null=True, blank=True, verbose_name='Прочее')

    class Meta:
        verbose_name_plural = 'Сайты_Квазар'
        verbose_name = 'Сайт'
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class PhoneBook(models.Model):
    title = models.CharField(max_length=70, verbose_name='Район')
    phone = models.TextField(null=True, blank=True, verbose_name='Телефон')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name_plural = 'Телефоны сетей'
        verbose_name = 'телефон'
        ordering = ['title']

    def __str__(self):
        return self.title


class DutyShedule(models.Model):
    date = models.DateTimeField(auto_now_add=False, verbose_name='Дата дежурства')
    duty = models.TextField(null=True, blank=True, verbose_name='Дежурный')
    duty_add = models.TextField(null=True, blank=True, verbose_name='Группа дежурного')
    support = models.TextField(null=True, blank=True, verbose_name='Поддержка')
    support_add = models.TextField(null=True, blank=True, verbose_name='Группа поддержки')

    class Meta:
        verbose_name_plural = 'Дежурные'
        verbose_name = 'дежурный'
        ordering = ['date']

    def __str__(self):
        return self.date


class DutyTimetable(models.Model):
    date_start = models.DateTimeField(auto_now_add=False, verbose_name='Дата начала дежурства')
    date_end = models.DateTimeField(auto_now_add=False, verbose_name='Дата окончания дежурства')
    duty = models.TextField(null=True, blank=True, verbose_name='Дежурный')
    duty_add = models.TextField(null=True, blank=True, verbose_name='Группа дежурного')
    support = models.TextField(null=True, blank=True, verbose_name='Поддержка')
    support_add = models.TextField(null=True, blank=True, verbose_name='Группа поддержки')

    class Meta:
        verbose_name_plural = 'Дежурные'
        verbose_name = 'дежурный'
        ordering = ['date_start']

    def __str__(self):
        return self.date_start
