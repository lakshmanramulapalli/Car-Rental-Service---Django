from django.contrib import admin
from .models import Car, Service, Location, Testimonial, FAQ

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'car_type', 'seats', 'price_per_day', 'is_available')
    list_filter = ('car_type', 'is_available')
    search_fields = ('model', 'description')
    list_editable = ('is_available',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')
    search_fields = ('title', 'description')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'phone', 'email')
    search_fields = ('city', 'address')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating')
    list_filter = ('rating',)
    search_fields = ('name', 'content')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)

admin.site.register(Car, CarAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(FAQ, FAQAdmin)

