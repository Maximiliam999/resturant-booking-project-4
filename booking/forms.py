from django import forms 
from .models import Booking
from django.forms.widgets import DateInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class BookingForm(forms.ModelForm):
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget)
    class Meta:
        model = Booking
        fields = ('guests', 'date', 'time', 'name', 'phone', 'email', 'verify_length', 'verify_cancelation_policy')
        widgets = { 'date': DateInput(attrs={'type': 'date'})}
        
    
    