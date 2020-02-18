from django.contrib import admin
from preferences.admin import PreferencesAdmin

from ..models import Hotel


@admin.register(Hotel)
class HotelAdmin(PreferencesAdmin):
    exclude = ('sites', )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'address',
                'email',
                'phone',
                'rules',
                'time_in',
                'time_out',
                'place',
            ),
        }),
        ('Банковские реквизиты', {
            'classes': ('collapse', ),
            'fields': (
                'bank_detail_recipient',
                'bank_detail_inn',
                'bank_detail_kpp',
                'bank_detail_account',
                'bank_detail_bank_name',
                'bank_detail_bik',
                'bank_detail_cor_account',
            ),
        }),
    )

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        return super(HotelAdmin, self).change_view(request, object_id, form_url, extra_context)
