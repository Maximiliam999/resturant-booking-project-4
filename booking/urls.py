from .views import book_table, booking_successful
from django.urls import path 

urlpatterns = [
    path('book/', book_table, name='book_table'),
    path('booking-successful/', booking_successful, name='booking_successful'),
]