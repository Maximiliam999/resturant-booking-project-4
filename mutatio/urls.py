"""
URL configuration for mutatio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from landingpage import views as landing_views
from booking import views as booking_views
from menu import views as menu_views
from cancel import views as cancel_views

urlpatterns = [
    path('', landing_views.index, name='landing'),
    path('', booking_views.index, name='booking'),
    path('', menu_views.index, name='menu'),
    path('', cancel_views.index, name='cancel'),
    path('admin/', admin.site.urls),
]
