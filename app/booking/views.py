from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone
from django.utils.decorators import method_decorator
from .forms import BookingManageForm
from .utils import get_booking_table, GanttData
from ..rooms.models import Room
from .models import Booking


class IndexView(generic.TemplateView):
    template_name = 'booking/index.html'

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        try:
            period = abs(int(self.request.GET.get('period', 90)))
        except ValueError:
            period = 90
        else:
            if period < 1 or period > 90:
                period = 90
        now = timezone.now()
        start_date = now - timedelta(days=2)
        end_date = now + timedelta(days=period+2)

        kwargs.update({
            'now_date': now,
            'start_date': start_date,
            'end_date': end_date,
            'rooms': Room.objects.filter(is_active=True).values('id', 'name', 'category__name'),
            'booking': Booking.objects.filter(date_to__gte=start_date, date_from__lte=end_date),
        })
        return kwargs


@method_decorator(login_required(login_url='/manage/login'), name='dispatch')
class DashboardView(generic.TemplateView):
    template_name = 'manage/index.html'
    extra_context = {
        'title': 'Сетка брони',
        'title_icon': 'calendar alternate outline',
        'subtitle': 'Вся статистика по бронированию за текущий месяц',
    }

    def get_context_data(self, **kwargs):
        kwargs = super(DashboardView, self).get_context_data(**kwargs)
        booking_table = get_booking_table()
        kwargs.update({'booking_table': booking_table})
        return kwargs


@method_decorator(login_required(login_url='/manage/login'), name='dispatch')
class AddReservation(generic.CreateView):
    template_name = 'manage/add_reservation.html'
    form_class = BookingManageForm
    extra_context = {
        'title':  'Новое бронирование',
        'title_icon': 'calendar plus outline',
        'subtitle': 'Информация о заезде',
    }
