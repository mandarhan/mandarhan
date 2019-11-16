from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RoomsConfig(AppConfig):
    name = 'app.rooms'
    label = 'app_rooms'
    verbose_name = _("Rooms")
