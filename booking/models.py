from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
GUESTS = ((2, "Two"),(3, "Three"),(4, "Four"),(5, "Five"))

TIME_CHOICES = (
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    ("22:00", "22:00"),
    ("22:30", "22:30"),
    ("23:00", "23:30")
)

class Booking(models.Model):
    guests = models.IntegerField(choices=GUESTS, default=2)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default=False)
    name = models.CharField(max_length=200, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()
    verify_length = models.BooleanField(default=False)
    verify_cancelation_policy = models.BooleanField(default=False)
