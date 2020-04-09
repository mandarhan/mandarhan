from django.urls import path

from . import views
from ..booking import views as booking_views


urlpatterns = [
    path('', booking_views.DashboardView.as_view(), name='dashboard'),
    path('add-reservation', booking_views.AddReservation.as_view(), name='add-reservation'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
