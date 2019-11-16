from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    name = models.CharField(_('payment name'), max_length=120)
    my_order = models.PositiveSmallIntegerField(_('order'), default=0, blank=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['my_order', 'name']
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
