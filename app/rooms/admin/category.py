from django.contrib import admin
from ..models import Category

__all__ = [
    'CategoryAdmin',
]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
