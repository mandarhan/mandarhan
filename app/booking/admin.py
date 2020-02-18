from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('id', 'channel', 'date_from', 'date_to', 'room', 'status')
    list_filter = ('channel', 'date_from', 'date_to', 'status')
