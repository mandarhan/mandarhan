from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from .models import Booking
from ..rooms.models import Room, Category
from ..settings.models import Status


class BookingView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        now = timezone.now()
        data = []
        for booking in Booking.objects.filter(date_to__gte=now):
            data.append({
                'category': booking.room.category_id,
                'room': booking.room_id,
                'start_date': booking.date_from.strftime('%d-%m-%Y'),
                'end_date': booking.date_to.strftime('%d-%m-%Y'),
                'text': str(booking),
                'id': booking.id,
                'status': booking.status_id,
            })
        collections = {
            'bookingStatus': [],
            'room': [],
            'roomCategory': [],
        }
        for status in Status.objects.all():
            collections['bookingStatus'].append({
                'id': status.id,
                'value': status.id,
                'label': status.name,
            })
        for room in Room.objects.all():
            collections['room'].append({
                'id': room.id,
                'value': room.id,
                'label': room.name,
                'category': room.category_id
            })
        for category in Category.objects.all():
            collections['roomCategory'].append({
                'id': category.id,
                'value': category.id,
                'label': category.name,
            })
        result = {
            'data': data,
            'collections': collections,
        }
        return Response(result)
