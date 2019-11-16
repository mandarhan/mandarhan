from django.contrib import admin
from ..models import Room

__all__ = [
    'RoomAdmin',
]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass