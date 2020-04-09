import datetime
from django import template

register = template.Library()


@register.filter
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


@register.filter
def daterangemonth(start_date, end_date):
    counter = dict()
    dates = list()
    month_year = list()
    for n in range(int((end_date - start_date).days)):
        date = start_date + datetime.timedelta(n)
        if (date.month, date.year) not in month_year:
            month_year.append((date.month, date.year))
            dates.append(date)
            try:
                counter[date.year][date.month] = 1
            except KeyError:
                counter[date.year] = {date.month: 1}
        else:
            counter[date.year][date.month] += 1
    for date in dates:
        yield date, counter[date.year][date.month]
