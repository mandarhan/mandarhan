from django.db import models
from django.utils.translation import gettext_lazy as _


class Channel(models.Model):
    OTA_CHOICES = (
        (0, 'свободный'),
        (1, 'Ostrovok.ru'),
        (2, 'Booking.com'),
    )

    name = models.CharField(_('name'), max_length=60)
    ota = models.PositiveSmallIntegerField('Канал продаж', default=0, choices=OTA_CHOICES)
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    email = models.CharField(_('email'), max_length=128, blank=True, null=True)
    address = models.TextField(_('address'), blank=True, null=True)
    contact_name = models.CharField(_('contact name'), max_length=128, blank=True, null=True)
    discount = models.DecimalField(_('client discount'), max_digits=2, decimal_places=0, default=0)
    commission = models.DecimalField(_('commission percent'), max_digits=2, decimal_places=0, default=0)
    my_order = models.PositiveSmallIntegerField(_('order'), default=0, blank=True, null=False)

    class Meta:
        verbose_name = 'источник бронирования'
        verbose_name_plural = 'источники бронирования'
        ordering = ['my_order']

    def __str__(self):
        return self.name
