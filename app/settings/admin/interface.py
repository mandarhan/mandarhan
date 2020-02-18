from django.contrib import admin
from preferences.admin import PreferencesAdmin

from ..models import Interface


@admin.register(Interface)
class InterfaceAdmin(PreferencesAdmin):
    exclude = ('sites', )

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        return super(InterfaceAdmin, self).change_view(request, object_id, form_url, extra_context)
