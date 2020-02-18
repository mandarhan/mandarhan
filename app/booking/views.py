from datetime import datetime
from django.views import generic
from django.utils import timezone
from ..rooms.models import Category


class IndexView(generic.TemplateView):
    template_name = 'booking/index.html'

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        booking_table = []
        for category in categories:
            add_room = True
            booking_table.append({
                'name': category.name
            })
            for room in category.room_set.all():
                values = []
                if room.booking_set.filter(date_to__gte=timezone.now()).count():
                    for value in room.booking_set.filter(date_to__gte=timezone.now()):
                        values.append({
                            'from': value.date_from.strftime('%Y/%m/%d'),
                            'to': value.date_to.strftime('%Y/%m/%d'),
                        })
                if add_room:
                    booking_table[-1]['desc'] = room.name
                    booking_table[-1]['values'] = values
                    add_room = False
                else:
                    booking_table.append({
                        'desc': room.name,
                        'values': values
                    })

        kwargs.update({'booking_table': booking_table})
        return kwargs
