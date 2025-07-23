from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'pickup_city', 'start_date', 'end_date', 'total_price', 'status')
    list_filter = ('status', 'start_date', 'pickup_city')
    search_fields = ('user__username', 'car__model', 'pickup_city')
    list_editable = ('status',)
    date_hierarchy = 'start_date'

admin.site.register(Booking, BookingAdmin)

