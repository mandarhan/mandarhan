from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PageConfig(AppConfig):
    name = 'app.pages'
    label = 'app_pages'
    verbose_name = _('pages')
