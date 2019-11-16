import os
import uuid
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

__all__ = [
    'Category',
]


class Category(models.Model):
    """
    Класс модели управления категориями номеров
    """
    PRICE_TYPE_CHOICES = (
        (1, _('per room')),
        (2, _('per person'))
    )
    name = models.CharField(_("category name"), max_length=120)
    main_places = models.PositiveIntegerField(_("main places"), default=1)
    additional_places = models.PositiveIntegerField(_("additional places"), default=0)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2, default=0)
    price_type = models.IntegerField(_('price_type'), default=1, choices=PRICE_TYPE_CHOICES)
    additional_price = models.DecimalField(
        _("price for additional place"),
        max_digits=8,
        decimal_places=2,
        default=0
    )
    allow_external_booking = models.BooleanField(_("allow external booking"), default=False)
    
    # Модуль бронирования
    widget_name = models.CharField(
        _("widget category name"),
        max_length=120, 
        null=True, 
        blank=True
    )
    widget_description = models.TextField(
        _("widget category description"),
        null=True, 
        blank=True
    )
    room_size = models.PositiveIntegerField(_("room size"), null=True, blank=True)
    amenities = models.ManyToManyField(
        'Amenity', 
        through='CategoryAmenities',
        verbose_name=_("room amenities"),
    )
    additional_services = models.ManyToManyField(
        "app_settings.Service",
        through='CategoryServices', 
        verbose_name=_("additional services"),
    )
    payments = models.ManyToManyField(
        "app_settings.Payment",
        through='CategoryPayments',
        verbose_name=_('allow payment options'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['name']


class CategoryAmenities(models.Model):
    amenity = models.ForeignKey("Amenity", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CategoryServices(models.Model):
    service = models.ForeignKey("app_settings.Service", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CategoryPhotos(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(
        _('category photo'), 
        upload_to=lambda instance, filename: str('category/%i/%s.%s' % (instance.id, uuid.uuid4(), filename.split('.')[-1]))
    )

    class Meta:
        ordering = ['-pk']


class CategoryPayments(models.Model):
    payment = models.ForeignKey("app_settings.Payment", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


@receiver(models.signals.post_delete, sender=CategoryPhotos)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удаляет файлы в хранилище когда объект модели удаляется.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=CategoryPhotos)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Удаляет старый файл в хранилище, когда обновляется объект модели.
    """
    if not instance.pk:
        return False

    try:
        old_photo = CategoryPhotos.objects.get(pk=instance.pk).photo
    except CategoryPhotos.DoesNotExist:
        return False

    new_photo = instance.photo
    if not old_photo == new_photo:
        if os.path.isfile(old_photo.path):
            os.remove(old_photo.path)
