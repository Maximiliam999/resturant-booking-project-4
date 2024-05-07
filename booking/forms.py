from django import forms 
from .models import Booking
from django.forms.widgets import DateInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guests', 'date', 'time', 'name', 'phone', 'email', 'verify_length', 'verify_cancelation_policy')
        widgets = { 'date': DateInput(attrs={'type': 'date'})}