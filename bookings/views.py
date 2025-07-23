
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking has been cancelled successfully.')
    else:
        messages.error(request, 'Only pending bookings can be cancelled.')
    return redirect('booking_list')