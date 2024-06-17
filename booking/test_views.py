from django.test import TestCase, Client
from .forms import CancellationBookingForm, BookingForm
from . models import Booking, CancelBooking
from django.urls import reverse
from datetime import date, timedelta

class TestBookingViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_booking_url = reverse('create_booking')
        self.create_booking_url = reverse('cancel_bookings')
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
        response = self.client.post(self.create_booking_url, self.booking_form)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(name='Testy Test').exists())
        self.assertRedirects(response, reverse('home')+ '?reservation=succes')
    
    def test_booking_max_reservations(self):
        for _ in range(Max_reservations):
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
        self.assertIn('Sadly Max Reservations Met Pick Another Time Or Day!', response.content.decode())

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
    self.assertIn('Sadly Max Occupancy Met Pick Another Time Or Day!', response.content.decode())

    def test_cancellation_policy_invalid(self):
        booking_form_policy_invalid = self.booking_form.copy()
        booking_form_policy_invalid['verify_cancellation_policy'] = False
        response = self.client.post(self.create_booking_url, booking_form_policy_invalid)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please accept the cancellation policy before booking', response.content.decode())
        self.assertFalse(Booking.objects.filter(name='Testy Test').exists())
 
