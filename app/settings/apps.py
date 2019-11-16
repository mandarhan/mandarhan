from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SettingsConfig(AppConfig):
    name = 'app.settings'
    label = 'app_settings'
    verbose_name = _('settings')
