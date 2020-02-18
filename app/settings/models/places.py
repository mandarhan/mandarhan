from django.db import models
from django.utils.translation import gettext_lazy as _


class Place(models.Model):
    name = models.CharField(_('name'), max_length=60)
    my_order = models.PositiveSmallIntegerField(_('order'), default=0, blank=True, null=False)

    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')
        ordering = ['my_order']

    def __str__(self):
        return self.name
