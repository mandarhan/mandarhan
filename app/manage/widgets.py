from django.forms import widgets


class CalendarInput(widgets.Input):
    input_type = 'text'
    template_name = 'manage/forms/widgets/calendar.html'
