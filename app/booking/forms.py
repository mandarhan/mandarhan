from django import forms
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
