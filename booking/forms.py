from .models import Booking
from django import forms 


class BookingForm(forms.ModelForm):
    class meta:
        model = Booking
        fields = ('guests', 'date', 'time', 'name', 'phone', 'email', 'verify_length', 'verify_cancelation_policy')