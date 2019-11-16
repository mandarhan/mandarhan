from django.shortcuts import render
from django.http import HttpRequest


def page_not_found(request: HttpRequest, exception: dict) -> render:
    return render(request, '404.html', status=404)
