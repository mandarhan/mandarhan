from django.contrib import admin
from ..models import Amenity

__all__ = [
    'AmenityAdmin',
]


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
