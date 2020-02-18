from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass
