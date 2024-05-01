from django.shortcuts import render,redirect
from django.views import generic
from .models import Booking
from .forms import BookingForm 
from django.contrib import messages
from django.db.models import Count

# Create your views here.

Max_reservations = 20
    
def book_table(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            date = form.cleand_data['date']
            time = form.cleand_data['time']
            reservations = BookingReservation.objects.filter(date=date, time=time).count()
            if reservations >= Max_reservations:
                messages.add_message(
                    request, messages.SUCCESS,
                    'All Tables Full At This Time And Date'
                )
                return render(request, 'create_booking.html')
                booking_form.save()
            else:
                booking_form = BookingForm
            

            booking_form = BookingForm()

def booking_successful(request):
    messages.add_message(
    request, messages.SUCCESS,
    'Reservation Successful!'
    )
    return render(request,
    'booking/booking.html',
    {"booking": booking,
    'booking_form':booking_form}
    )
