from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('locations/', views.locations, name='locations'),
    path('contact/', views.contact, name='contact'),
    path('cars/', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
]