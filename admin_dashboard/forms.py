from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from booking.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'guests', 'date', 'time', 'name', 'phone', 'email', 'verify_cancellation_policy']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
        }

class CancelBookingForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']