from django.urls import path

from .. import api

urlpatterns = [
    path('', api.BookingView.as_view(), name='booking-list')
]
