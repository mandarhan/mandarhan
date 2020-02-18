from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BookingConfig(AppConfig):
    name = 'app.booking'
    label = 'app_booking'
    verbose_name = _('Booking')
