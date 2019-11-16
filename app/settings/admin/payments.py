from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from ..models import Payment


@admin.register(Payment)
class PaymentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'my_order')
