

from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from main.models import Car


class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.car.model} by {self.user.username}"

    def duration(self):
        return (self.end_date - self.start_date).days

    def save(self, *args, **kwargs):
        if not self.pk:  # Only for new bookings
            duration = self.duration()
            self.total_price = duration * self.car.price_per_day
        super().save(*args, **kwargs)