from . import views
from django.urls import path 

urlpatterns = [
    path('book/', views.create_booking, name='booking'),
]