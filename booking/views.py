from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from django.views import generic
from .models import Booking, CancelBooking
from .forms import BookingForm, CancellationBookingForm
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
                request, messages.ERROR,
                'All Tables Are Full At This Time Try Another Day Or Time!'
                )
            else:
                booking = booking_form.save()
                #send email to verify
                send_email_verification(booking) 
                messages.add_message(
                request, messages.SUCCESS,
                'Reservation Successful!'
                )
                return redirect(reverse('home') + '?reservation=succes')
    else:
        booking_form = BookingForm()
    
    return render(request,
    'booking/create_booking.html',
    {'booking_form':booking_form})


def send_email_verification(booking):
    subject  = 'Reservation Confirmed'
    message = 'Your reservation has been confirmed'
    recipient_email = booking.email
    send_mail(subject, message, 'nuitnoire01@hotmail.com', [recipient_email])

def cancel_bookings(request):
    if request.method == 'POST':
        cancellation_form = CancellationBookingForm(data=request.POST)
        if cancellation_form.is_valid():
            name = cancellation_form.cleaned_data['name']
            phone = cancellation_form.cleaned_data['phone']
            try:
                booking_to_cancel = Booking.objects.get(name=name, phone=phone)
                booking_to_cancel.delete()
                messages.add_message(
                request, messages.SUCCESS,
                'Your Reservation Has Been Cancelled')
                return redirect(reverse('home') + '?reservation=succes')
            except Booking.DoesNotExist:
                messages.add_message(
                request, messages.ERROR,
                'No Booking Found With The Name And Phone Provided')
    else:
        cancellation_form = CancellationBookingForm()

    return render(request, 'booking/cancel_bookings.html', {'cancellation_form': cancellation_form})
