from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ClientsConfig(AppConfig):
    name = 'app.clients'
    label = 'app_clients'
    verbose_name = _('clients')
