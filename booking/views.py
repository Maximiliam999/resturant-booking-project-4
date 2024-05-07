from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.views import generic
from .models import Booking
from .forms import BookingForm 
from django.contrib import messages
from django.db.models import Count

# Create your views here.

Max_reservations = 1
    
def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            date = booking_form.cleaned_data['date']
            time = booking_form.cleaned_data['time']
            reservations = Booking.objects.filter(date=date, time=time).count()
            if reservations >= Max_reservations:
                messages.add_message(
                request, messages.SUCCESS,
                'All Tables Are Full At This Time Try Another Day Or Time!'
                )
            else:
                booking_form.save()
                #send email to verify
                send_email_verification(booking) 
                messages.add_message(
                request, messages.SUCCESS,
                'Reservation Successful!'
                )
                       
    else:
        booking_form = BookingForm()
    
    return render(request,
    'booking/create_booking.html',
    {'booking_form':booking_form})

def booking_successful(request):
    return render(request, 'booking_succesful.html')

def send_email_verification(booking):
    subject  = 'Reservation Confirmed'
    message = 'Your reservation has been confirmed'
    recipient_email = booking.email
    send_mail(subject, message, 'nuitnoire01@hotmail.com', [recipient_email])