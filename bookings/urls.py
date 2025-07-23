from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]