from django import forms
from booking.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'guests', 'date', 'time', 'name', 'phone', 'email', 'verify_cancellation_policy']

class CancelBookingForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)