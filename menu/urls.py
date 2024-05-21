from django.contrib import admin
from menu import views
from django.urls import path 

urlpatterns = [
    path('', views.menu, name='menu'),
]