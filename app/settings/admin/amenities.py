from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from ..models import Amenity


@admin.register(Amenity)
class AmenityAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'my_order')
    prepopulated_fields = {'code': ('name',), }
