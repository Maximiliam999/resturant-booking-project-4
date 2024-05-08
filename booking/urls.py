from . import views
from django.urls import path 

urlpatterns = [
    path('book/', views.create_booking, name='booking'),
    path('cancel/', views.cancel_bookings, name='cancel_bookings')
]