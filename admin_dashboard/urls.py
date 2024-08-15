from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('login/', views.login, name='adminlogin'),
    path('book/', views.create_booking, name='create_booking'),
    path('cancel/', views.cancel_booking, name='cancel_booking'),
    path('bookings/', views.list_bookings, name='list_bookings'),
    path('bookings/<int:pk>/edit/', views.edit_booking, name='edit_booking'),
    path('bookings/<int:pk>/delete/', views.delete_booking, name='delete_booking'),
]