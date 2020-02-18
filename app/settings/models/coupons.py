from django.db import  models
from django.utils.translation import gettext_lazy as _


class Coupon(models.Model):
    PRICE_TYPE_CHOICES = (
        (0, '%'),
        (1, 'руб.')
    )
    name = models.CharField(_('name'), max_length=128)
    code = models.CharField(_('code'), max_length=128)
    limit = models.PositiveIntegerField('Лимит использования', default=0, help_text='0 - без ограничений.')
    date_from = models.DateField('Срок действия от', help_text='Если пусто - без ограничения.', blank=True, null=True)
    date_to = models.DateField(
        'Срок действия до',
        help_text='Если пусто - без ограничения, в указанную дату купон уже не действует.',
        blank=True, null=True
    )
    price = models.DecimalField(_('discount'), max_digits=19, decimal_places=2)
    price_type = models.PositiveSmallIntegerField(_('price type'), default=0, choices=PRICE_TYPE_CHOICES)
    active = models.BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _('coupon')
        verbose_name_plural = _('coupons')

    def __str__(self):
        return self.name
