from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ManageConfig(AppConfig):
    name = 'app.manage'
    label = 'app_manage'
    verbose_name = _('manage')
