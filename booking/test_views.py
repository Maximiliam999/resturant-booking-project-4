from django.test import TestCase, Client
from .forms import CancellationBookingForm, BookingForm
from . models import Booking, CancelBooking
from django.urls import reverse
from datetime import date, timedelta
from django.contrib import messages

class TestBookingViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_booking_url = reverse('booking')
        self.cancel_booking_url = reverse('cancel_bookings')
        self.booking_form = {
            'guests': 2,
            'date': '2024-06-20',
            'time': '18:00',
            'name': 'Testy Test',
            'email': 'test@test.com',
            'phone': '+46736845312',
            'verify_cancellation_policy': True  
        }

    def test_create_booking_valid(self):
        response = self.client.post(self.create_booking_url, self.booking_form, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('home')+ '?reservation=succes')
        self.assertTrue(Booking.objects.filter(name='Testy Test').exists())
       
    
    def test_booking_max_reservations(self):
        for _ in range(10):
            Booking.objects.create(
                guests=2,
                date= '2024-06-20',
                time= '18:00',
                name=f"booking {_}",
                email=f"test{_}@test.com",
                phone= f"+46736845312{_}",
                verify_cancellation_policy= True
            )
        response = self.client.post(self.create_booking_url, self.booking_form)
        self.assertEqual(response.status_code, 200)


    def test_booking_max_guests(self):
        Booking.objects.create(
            guests=2,
            date= '2024-06-20',
            time= '18:00',
            name= 'Testy Test',
            email= 'test@test.com',
            phone= '+46736845312',
            verify_cancellation_policy= True
            )
        response = self.client.post(self.create_booking_url, self.booking_form)
        self.assertEqual(response.status_code, 200)


    def test_cancellation_policy_invalid(self):
        booking_form_policy_invalid = self.booking_form.copy()
        booking_form_policy_invalid['verify_cancellation_policy'] = False
        response = self.client.post(self.create_booking_url, booking_form_policy_invalid)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Booking.objects.filter(name='Testy Test').exists())

class TestCancelBookingViews(TestCase):
    def setUp(self):
        self.clinet = Client()
        self.cancel_bookings_url = reverse('cancel_bookings')
        self.booking = Booking.objects.create(
            guests=2,
            date= '2024-06-20',
            time= '18:00',
            name= 'Testy Test',
            email= 'test@test.com',
            phone= '+46736845312',
            verify_cancellation_policy= True
        )
        self.cancellation_form = {
            'name': 'Testy Test',
            'phone': '+46736845312'
        }

    def test_cancel_bookings_valid(self):
        response = self.client.post(self.cancel_bookings_url, self.cancellation_form)
        self.assertEqual(response.status_code, 302) #redirected to 'home'
        self.assertFalse(Booking.objects.filter(name='Testy Test').exists())
        self.assertRedirects(response, reverse('home') + '?reservation=succes')
    
    def test_cancel_bookings_invalid(self):
        cancellation_form_invalid = {
            'name': 'Booking Nonexistent',
            'phone': '+46736845312'
        }
        response = self.client.post(self.cancel_bookings_url, cancellation_form_invalid)
        self.assertEqual(response.status_code, 200)
