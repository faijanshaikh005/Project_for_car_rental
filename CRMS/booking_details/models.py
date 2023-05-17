from django.db import models

# Create your models here.

# Create your models here.
class Car_Booking_details(models.Model):
    Pick_up_date = models.DateField()
    Drop_off_date = models.DateField()
    car_name = models.CharField(max_length=122)
    car_company_name = models.CharField(max_length=122)
    car_rent_per_day = models.IntegerField()
    Car_type = models.CharField(max_length=122)
   
