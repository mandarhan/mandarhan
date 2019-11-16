from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    PRICE_TYPE_CHOICES = (
        (0, 'единоразово'),
        (1, 'в сутки'),
        (2, 'в сутки / за человека'),
        (3, 'за человека'),
        (4, 'скидка в %'),
    )
    name = models.CharField(_("service name"), max_length=160)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2, default=0)
    price_type = models.IntegerField(_('price type'), choices=PRICE_TYPE_CHOICES, default=0)
    maximum = models.IntegerField(_('maximum value'), null=True, blank=True)
    exclude_services = models.ManyToManyField('Service', verbose_name=_('exclude services'), blank=True)
    allow_apply_only_full_room = models.BooleanField(_('allow apply only full room'), default=False)
    my_order = models.PositiveSmallIntegerField(_('order'), default=0, blank=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['my_order', 'name']
        verbose_name = _("service")
        verbose_name_plural = _("services")
