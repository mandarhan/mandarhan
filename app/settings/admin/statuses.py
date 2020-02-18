from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableAdminMixin

from ..models import Status


@admin.register(Status)
class StatusAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'show_color')

    def show_color(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 45px; height: 12px; border: 1px dashed #000;"></div>',
            obj.color
        )
    show_color.short_description = _('color')
