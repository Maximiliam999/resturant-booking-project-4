from . import views
from django.urls import path 

urlpatterns = [
    path('book/', views.create_booking, name='booking'),
    # path('booking_succesful/', views.booking_successful, name='booking_succesful')
]