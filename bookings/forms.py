from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from main.models import Car
import datetime

class BookingForm(forms.ModelForm):
    pickup_city = forms.CharField(max_length=100)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['pickup_city', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date < datetime.date.today():
                raise ValidationError("Start date cannot be in the past")
            if end_date < start_date:
                raise ValidationError("End date must be after start date")

            # Check if the duration is more than 30 days (optional)
            if (end_date - start_date).days > 30:
                raise ValidationError("Maximum rental duration is 30 days")

        return cleaned_data


