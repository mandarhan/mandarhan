from django.db import models
from django.utils import timezone
from django.utils.formats import date_format
from django.urls import reverse


class Booking(models.Model):
    PRICE_TYPE_CHOICES = (
        (1, 'за сутки'),
        (2, 'за месяц'),
        (3, 'за час'),
        (4, 'за всё время'),
        (5, 'за 30 дней'),
    )
    channel = models.ForeignKey('app_settings.Channel', verbose_name='Источник брони', on_delete=models.PROTECT)
    channel_booking_number = models.CharField('Номер брони у источника', max_length=60, null=True, blank=True)
    date_from = models.DateTimeField('Заезд')
    date_to = models.DateTimeField('Выезд')
    room = models.ForeignKey('app_rooms.Room', verbose_name='Номер', on_delete=models.PROTECT)
    price = models.DecimalField('Стоимость проживания', max_digits=8, decimal_places=2, default=0)
    price_type = models.IntegerField('Стоимость за', choices=PRICE_TYPE_CHOICES, default=1)
    person = models.IntegerField('Основных мест', default=1)
    person_additional = models.IntegerField('Доп. мест', default=0)
    status = models.ForeignKey('app_settings.Status', verbose_name='Статус', null=True, blank=True,
                               on_delete=models.SET_NULL)
    comment = models.TextField('Комментарий администратора', null=True, blank=True)
    client_comment = models.TextField('Пожелания клиента', null=True, blank=True)
    created_at = models.DateTimeField('Дата добавления брони', default=timezone.now)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Брони'
        ordering = ['-date_from', '-date_to']

    def __str__(self):
        return 'Бронь №{} от {}'.format(self.id, date_format(self.created_at, format='SHORT_DATE_FORMAT'))

    def get_absolute_url(self):
        return reverse('app:dashboard')
