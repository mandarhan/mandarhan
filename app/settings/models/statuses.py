from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Status(models.Model):
    name = models.CharField(_('name'), help_text='назваие статуса проживания', max_length=60)
    color = ColorField(verbose_name=_('color'), default='#000000')
    my_order = models.PositiveSmallIntegerField(_('order'), default=0, blank=True, null=False)

    class Meta:
        verbose_name = _('residence status')
        verbose_name_plural = _('residence statuses')
        ordering = ['my_order']

    def __str__(self):
        return self.name
