from django.test import TestCase 
from unittest.mock import patch
from .forms import CancellationBookingForm, BookingForm

class TestBookingForm(TestCase):
    def test_form_is_valid(self):
        """ Test for all fields"""
        form = BookingForm({
            'guests': 5,
            'name': 'Testy Test',
            'date': '2024-06-20',
            'time': '18:00',
            'phone': '+46736845311',
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
            'phone': '46736845311',
            'email': 'test@test.com',
            'verify_cancellation_policy': True,
        })
        self.assertFalse(
            form.is_valid(),
            msg = 'Form should be invalid with wrong phone number format is used '
        )

    
    