from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableAdminMixin

from ..models import Channel


@admin.register(Channel)
class StatusAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'ota', 'my_discount', 'my_commission', 'phone', 'contact_name', 'my_order')
    list_display_links = ('name',)

    def has_change_permission(self, request, obj=None):
        if obj and obj.id == 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.id == 1:
            return False
        return True

    def my_discount(self, obj=None):
        return '%s%%' % obj.discount
    my_discount.short_description = _('discount')

    def my_commission(self, obj=None):
        return '%s%%' % obj.commission
    my_commission.short_description = _('commission')
