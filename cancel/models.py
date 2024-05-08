from django.db import models
from booking.models import Booking 
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

# Remove a instance of the booking model
class Cancel(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    cancelled_name = models.TextField()
    cancelled_phone = PhoneNumberField()
    cancelled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cancellation for: {self.booking.name} | Reason {self.cancel_reason}"