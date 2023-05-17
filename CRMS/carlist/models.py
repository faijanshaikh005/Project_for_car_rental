from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class cars(models.Model):
    car_company_name=models.CharField(max_length=50)
    car_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="pics",default="default.png")
    car_type=models.CharField(max_length=50)
    rent_per_day=models.IntegerField(default=0)