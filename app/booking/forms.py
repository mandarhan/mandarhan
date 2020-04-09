from django import forms
from django.db.models import Q
from django.utils.formats import date_format
from .models import Booking
from ..settings.models import Channel, Status
from ..rooms.models import Room
from ..manage.widgets import CalendarInput


class BookingManageForm(forms.ModelForm):
    channel = forms.ModelChoiceField(
        queryset=Channel.objects.all(),
        initial=Channel.objects.first(),
        widget=forms.Select(attrs={'class': 'ui fluid dropdown'}),
        label='Источник брони'
    )
    channel_booking_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Номер брони у источника'})
    )
    room = forms.ModelChoiceField(
        queryset=Room.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'ui fluid dropdown'}),
        label='Номер'
    )
    date_from = forms.DateTimeField(
        label='Дата заезда',
        widget=CalendarInput(),
    )
    date_to = forms.DateTimeField(
        label='Дата выезда',
        widget=CalendarInput(),
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        initial=Status.objects.first(),
        widget=forms.Select(attrs={'class': 'ui fluid dropdown'}),
        label='Статус брони'
    )
    price_type = forms.IntegerField(
        widget=forms.Select(
            choices=Booking.PRICE_TYPE_CHOICES,
            attrs={'class': 'ui fluid dropdown'},
        ),
    )

    class Meta:
        model = Booking
        fields = [
            'channel',
            'channel_booking_number',
            'room',
            'date_from',
            'date_to',
            'status',
            'price',
            'price_type',
            'comment',
            'client_comment',
        ]

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')
        reserved = room.booking_set.filter(
            Q(date_from__range=(date_from, date_to)) |
            Q(date_to__range=(date_from, date_to)) |
            Q(date_from__lte=date_from, date_to__gte=date_to)
        ).first()
        if reserved:
            self.add_error('date_from', 'Эта дата занята для выбранного номера, подробности ниже.')
            self.add_error('date_to', 'Эта дата занята для выбранного номера, подробности ниже.')
            raise forms.ValidationError(
                '{room} забронирован(а) с {date_from} до {date_to}'.format(
                    room=room.name,
                    date_from=date_format(reserved.date_from),
                    date_to=date_format(reserved.date_to),
                )
            )
