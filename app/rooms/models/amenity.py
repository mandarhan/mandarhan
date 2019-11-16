from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    'Amenity',
]


class Amenity(models.Model):
    """
    Класс модели уплавления удобствами в номерах
    """
    name = models.CharField(_("room amenity"), max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Amenity")
        verbose_name_plural = _("Amenities")
        ordering = ['name']
