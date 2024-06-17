from django.test import TestCase 
from unittest.mock import patch
from .forms import CancellationBookingForm, BookingForm
from .models import Booking, CancelBooking
from datetime import date

class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = BookingForm({
            'guests': 5,
            'name': 'Testy Test',
            'date': '2024-06-20',
            'time': '18:00',
            'phone': '+46736845312',
            'email': 'test@test.com',
            'verify_cancellation_policy': True,
        }) 

        self.assertTrue(form.is_valid(), msg=f'Form Errors: {form.errors}')

    def test_invalid_phone_number(self):
        """ Name Required """
        form = BookingForm({
            'guests': 5,
            'name': 'Testy Test',
            'date': '2024-06-20',
            'time': '18:00',
            'phone': '46736845312',
            'email': 'test@test.com',
            'verify_cancellation_policy': True,
        })
        self.assertFalse(
            form.is_valid(),
            msg = 'Form should be invalid with wrong phone number format is used '
        )

    def test_invalid_cancellation_form(self):
        """must accept cancellation agreement"""
        form = BookingForm({
            'guests': 5,
            'name': 'Testy Test',
            'date': '2024-06-20',
            'time': '18:00',
            'phone': '46736845312',
            'email': 'test@test.com',
            'verify_cancellation_policy': False,
        })
        self.assertFalse(
            form.is_valid(),
            msg = 'Form should be invalid when the user has not checked the cancellation policy'
        )

    
class TestCancellationBookingForm(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create (
            guests = 2,
            date = '2024-06-20',
            time = '18:00',
            name = 'Testy Test',
            email = 'test@test.com',
            phone = '+46736845312',
            verify_cancellation_policy=True  
        )    

    def test_valid_cancellation_booking_form(self):
        form = CancellationBookingForm({
            'name': 'Testy Test',
            'phone': '+46736845312'
        })
        self.assertTrue(
            form.is_valid(),
            msg = 'Form Cancellatio is valid'
        )
        cancellation = form.save(commit=False)
        cancellation.booking = self.booking
        cancellation.save()
        self.assertEqual(cancellation.name, 'Testy Test')
        self.assertEqual(cancellation.phone, '+46736845312')
    
    def test_invalid_cancellation_form(self):
        form = CancellationBookingForm({
            'name': 'Testy Test',
            'phone': '46736845312'
        })
        self.assertFalse(
            form.is_valid(),
            msg = 'Form cancellation invalid with wrong phone input'
        )

    def test_invalid_cancellation_form_name(self):
        form = CancellationBookingForm({
            'name': '',
            'phone': '+46736845312'
        })
        self.assertFalse(
            form.is_valid(),
            msg = 'Form cancellation invalid with wrong name input'
        )