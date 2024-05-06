from django import forms 
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guests', 'date', 'time', 'name', 'phone', 'email', 'verify_length', 'verify_cancelation_policy')