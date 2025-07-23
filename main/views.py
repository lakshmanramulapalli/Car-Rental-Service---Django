

from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Service, Location, Testimonial, FAQ
from bookings.forms import BookingForm


def home(request):
    featured_cars = Car.objects.filter(is_available=True).order_by('?')[:6]
    services = Service.objects.all()[:4]
    testimonials = Testimonial.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)[:5]

    context = {
        'featured_cars': featured_cars,
        'services': services,
        'testimonials': testimonials,
        'faqs': faqs,
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')


def services(request):
    all_services = Service.objects.all()
    return render(request, 'main/services.html', {'services': all_services})


def locations(request):
    all_locations = Location.objects.all()
    return render(request, 'main/locations.html', {'locations': all_locations})


def contact(request):
    return render(request, 'main/contact.html')


def car_list(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, 'main/car_list.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.car = car
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'main/car_detail.html', {'car': car, 'form': form})