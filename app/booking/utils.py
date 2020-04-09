import json
from django.utils import timezone
from ..rooms.models import Category, Room
from .models import Booking


class GanttData:
    def __init__(self, json=True):
        self.now = timezone.now()
        self.json = json

    @property
    def get_booking(self):
        data = []
        for booking in Booking.objects.filter(date_to__gte=self.now):
            start_date = booking.date_from.strftime('%d-%m-%Y')
            nights = booking.date_to - booking.date_from
            duration = nights.days
            progress = 0
            if self.now > booking.date_from:
                delta = self.now - booking.date_from
                progress = delta.days / nights.days
            data.append({
                'id': booking.id,
                'text': str(booking),
                'start_date': start_date,
                'duration': duration,
                'progress': progress,
                'room': booking.room_id,
                'category': booking.room.category_id
            })
            if self.json:
                return json.dumps(data)
            return data

    @property
    def get_rooms(self):
        data = []
        for room in Room.objects.all().values('id', 'name'):
            data.append({
                'key': room['id'],
                'label': room['name']
            })
        if self.json:
            return json.dumps(data)
        return data

    @property
    def get_categories(self):
        data = []
        for category in Category.objects.all().values('id', 'name'):
            data.append({
                'key': category['id'],
                'label': category['name']
            })
        if self.json:
            return json.dumps(data)
        return data

    @property
    def get_rooms_categories(self):
        data = []
        for room in Room.objects.all():
            data.append({
                'key': room.id,
                'label': room.name,
                'category': room.category_id,
            })
        for category in Category.objects.values('id', 'name'):
            data.append({
                'key': category['id'],
                'label': category['name']
            })
        return data


def get_booking_table():
    categories = Category.objects.all()
    datetime_now = timezone.now()
    booking_table = []
    for category in categories:
        booking_table.append({
            'id': category.id,
            'text': category.name,
            'start_date': '',
            'duration': 0,
            'progress': 0,
            'open': True
        })
        for room in category.room_set.filter(is_active=True):
            booking_table.append({
                'id': ''.join([str(category.id), str(room.id)]),
                'text': room.name,
                'start_date': '',
                'duration': 0,
                'progress': 0,
                'parent': category.id,
                'open': True,
            })
            for reserved in room.booking_set.filter(date_to__gte=datetime_now):
                start_date = reserved.date_from.strftime('%d-%m-%Y')
                nights = reserved.date_to - reserved.date_from
                duration = nights.days
                progress = 0
                if datetime_now > reserved.date_from:
                    delta = datetime_now - reserved.date_from
                    progress = delta.days / nights.days
                booking_table.append({
                    'id': ''.join([str(category.id), str(room.id), str(reserved.id)]),
                    'text': str(reserved),
                    'start_date': start_date,
                    'duration': duration,
                    'progress': progress,
                    'parent': ''.join([str(category.id), str(room.id)])
                })
    return json.dumps(booking_table)
