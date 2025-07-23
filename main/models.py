

from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    CAR_TYPE_CHOICES = (
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('luxury', 'Luxury'),
        ('sports', 'Sports'),
    )

    model = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    seats = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.model} ({self.get_car_type_display()})"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class")

    def __str__(self):
        return self.title


class Location(models.Model):
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.city


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} - {self.role}"


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question