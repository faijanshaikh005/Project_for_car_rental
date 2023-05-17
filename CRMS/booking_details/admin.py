from django.contrib import admin
from .models import Car_Booking_details

# Register your models here.
@admin.register(Car_Booking_details)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Car_Booking_details._meta.get_fields()]