import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from preferences.models import Preferences

from .places import Place


class Hotel(Preferences):
    # Основные настройки
    name = models.CharField(_('name'), max_length=128, default='ООО "5 звезд"')
    address = models.TextField(_('address'), default='Россия, Москва')
    email = models.EmailField(_('email'), default='info@mandarhan.com')
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    rules = models.TextField(
        _('terms and conditions of booking'),
        help_text=_('displayed in the reservation module'),
        blank=True, null=True
    )
    time_in = models.TimeField('Время заезда по умолчанию', default=datetime.time(13, 00))
    time_out = models.TimeField('Время выезда по умолчанию', default=datetime.time(12, 00))
    place = models.ForeignKey(
        'Place',
        verbose_name=_('place type'),
        on_delete=models.PROTECT,
        default=Place.objects.first().id
    )

    # Банковские реквизиты
    bank_detail_recipient = models.CharField('Получатель платежа', max_length=255, default='ООО "5 звезд"')
    bank_detail_inn = models.CharField('ИНН', max_length=12, default='123456789')
    bank_detail_kpp = models.CharField('КПП', max_length=9, blank=True, null=True, default='123456789')
    bank_detail_account = models.CharField('Номер счета', max_length=25, default='12345678912345678912')
    bank_detail_bank_name = models.CharField('Банк', max_length=255, default='Сбербанк')
    bank_detail_bik = models.CharField('БИК', max_length=9, default='123456')
    bank_detail_cor_account = models.CharField('Корреспондентский счёт', max_length=25, default='12345678912345678912')

    class Meta:
        verbose_name = 'объект размещения'
        verbose_name_plural = 'объекты размещения'
