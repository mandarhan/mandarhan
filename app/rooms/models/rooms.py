from django.db import models
from django.utils.translation import gettext_lazy as _

from ..uploaders import room_uploader

__all__ = [
    'Room',
]


class Room(models.Model):
    """
    Класс модели управления номерами
    """
    # Основные настройки
    name = models.CharField(_("room name"), max_length=60)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name=_("category"))
    main_places = models.PositiveIntegerField(_("main places"), default=1)
    additional_places = models.PositiveIntegerField(_("additional places"), default=0)
    price = models.DecimalField(
        _("price"), 
        max_digits=8, 
        decimal_places=2, 
        default=0
    )
    additional_price = models.DecimalField(
        _("price for additional place"),
        max_digits=8,
        decimal_places=2,
        default=0
    )
    allow_book_sleep_place = models.BooleanField(
        _("allow booking sleep place"),
        default=False
    )
    sleep_place_price = models.DecimalField(
        _("sleep place price"),
        max_digits=8,
        decimal_places=2,
        default=0
    )
    is_active = models.BooleanField(_("is active"), default=True)

    # Модуль бронирования
    export_name = models.CharField(_("export room name"), max_length=120, null=True, blank=True)
    export_description = models.TextField(_("export room description"), null=True, blank=True)
    room_size = models.PositiveIntegerField(_("room size"), null=True, blank=True)
    amenities = models.ManyToManyField(
        'app_settings.Amenity',
        verbose_name=_("room amenities"),
        blank=True
    )
    additional_services = models.ManyToManyField(
        "app_settings.Service",
        verbose_name=_('additional services'),
        blank=True
    )
    allow_external_booking = models.BooleanField(_("allow external booking"), default=True)
    room_payments = models.ManyToManyField(
        'app_settings.Payment',
        verbose_name=_('allow payment options'),
        blank=True
    )

    def __str__(self):
        return '{} | {}'.format(self.category, self.name)

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        ordering = ['name']


class RoomPhotos(models.Model):
    photo = models.ImageField(_("photo"), upload_to=room_uploader)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name=_("room"))

    class Meta:
        ordering = ['-pk']
