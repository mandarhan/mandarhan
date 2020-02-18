from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from ..models import Place


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
