from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from ..models import Service


@admin.register(Service)
class ServiceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'price_type', 'my_order')
    filter_horizontal = ('exclude_services',)
