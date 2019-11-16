from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Client, ClientPhotos


class ClientPhotosInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ClientPhotos
    extra = 1
    fields = ('client', 'photo_preview', 'photo', 'my_order')
    readonly_fields = ('photo_preview',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'is_foreigner', 'added_at')
    inlines = [ClientPhotosInline]
    list_filter = ('is_foreigner', ('birthday', DateRangeFilter), 'in_vip', 'in_blacklist',)
    search_fields = ('first_name', 'last_name', 'second_name', 'phone', 'email', 'comment')

