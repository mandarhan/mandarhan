from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
from preferences.models import Preferences


class Interface(Preferences):
    ON_OVER = 0
    ON_CLICK = 1
    BOOKING_TOOLTIP_CHOICES = (
        (ON_OVER, 'при наведении'),
        (ON_CLICK, 'при нажатии'),
    )

    NOT = 0
    RELATIVE = 1
    ACTUAL = 2
    PAYED_LAYER_CHOICES = (
        (NOT, 'нет'),
        (RELATIVE, 'относительный период'),
        (ACTUAL, 'фактический период'),
    )

    ON_CATEGORIES = 0
    NO_GROUP = 1
    ON_FLOORS = 2
    ON_CASES = 3
    ROOM_GROUP_CHOICES = (
        (ON_CATEGORIES, 'по категориям'),
        (ON_FLOORS, 'по этажам'),
        (ON_CASES, 'по корпусам'),
        (NO_GROUP, 'не группировать'),
    )

    booking_popup = models.BooleanField('открывать брони в отдельном окне', default=False)
    clean_mode = models.BooleanField('отображать статус уборки номера', default=True)
    booking_offset = models.BooleanField('смещать полоску бронирования на половину суток', default=True)
    show_calendar_foot = models.BooleanField('дублировать даты внизу шахматки', default=True)
    show_extra_data = models.BooleanField(
        'отображать дополнительные данные клиента на полоске бронирования', default=False
    )
    show_client_comment = models.BooleanField('отображать пожелания клиента в окне информации о брони', default=True)
    room_name_fixed = models.BooleanField('фиксировать названия номеров при горизонтальной прокрутке', default=True)
    not_payed_info = models.BooleanField(
        'помечать неоплаченные брони (для статусов "Проживание" и "Выезд")', default=True
    )
    comment_info = models.BooleanField('помечать брони с комментарием', default=True)
    audio_notify = models.BooleanField('включить звуковые уведомления', default=True)
    auto_price = models.BooleanField(
        'автоматически подставлять цену в поле "К оплате" при создании брони', default=True
    )
    auto_edit_price = models.BooleanField(
        'автоматически обновлять цену в поле "К оплате" при изменении брони', default=True
    )
    check_bl = models.BooleanField('автоматически проверять клиента по черному списку', default=True)
    support = models.BooleanField('включить онлайн-консультант', default=False)
    booking_tooltip = models.PositiveSmallIntegerField(
        'Показывать всплывающее окно с информацией о брони',
        default=ON_CLICK, choices=BOOKING_TOOLTIP_CHOICES
    )
    payed_layer = models.PositiveSmallIntegerField(
        'Выделять цветом период оплаты брони',
        default=ACTUAL, choices=PAYED_LAYER_CHOICES
    )
    payed_layer_stripe = models.BooleanField(
        'использовать штриховку', default=False
    )
    payed_layer_status = models.ManyToManyField(
        'Status', verbose_name='Выделять цветом период оплаты брони для статусов'
    )
    room_group = models.PositiveSmallIntegerField(
        'Группировать номера в шахматке',
        default=ON_CATEGORIES, choices=ROOM_GROUP_CHOICES
    )
    today_color = ColorField(default='#4ec8ea', verbose_name='Цвет линии текущего дня')
    payed_layer_color = ColorField(default='#009f1a', verbose_name='Цвет оплаченного периода на полоске бронирования')
    room_closed_color = ColorField(default='#7c7878', verbose_name='Цвет периода закрытого на ремонт номера')

    class Meta:
        verbose_name = _('Interface setting')
        verbose_name_plural = _('Interface settings')
