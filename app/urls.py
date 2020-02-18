from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
from rest_framework import views

app_name = 'app'

urlpatterns = [
    path('', include('app.pages.urls')),
    re_path(r'^manage/', include('app.manage.urls')),
    re_path(r'^plus/', include('app.booking.urls')),
    path(
        'robots.txt',
        TemplateView.as_view(
            content_type='text/plain',
            template_name='robots.txt'
        )
    )
]

apipaterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [path('api/', include((apipaterns, 'api'), namespace='api'))]
