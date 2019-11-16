from django.urls import path, re_path, include
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    path('', include('app.pages.urls')),
    path(
        'robots.txt',
        TemplateView.as_view(
            content_type='text/plain',
            template_name='robots.txt'
        )
    )
]
