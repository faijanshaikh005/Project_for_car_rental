from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=122)
    gender = (('M', 'Male'),('F', 'Female'),('O', 'Other'))
    gender = models.CharField(max_length=1, choices=gender)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    dateofbirth = models.DateField(max_length=8)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)
   
    