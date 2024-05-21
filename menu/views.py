from django.shortcuts import render,redirect
from django.views import generic



# Create your views here.


def menu(request):
    return render(request, 'menu/menu.html',)
