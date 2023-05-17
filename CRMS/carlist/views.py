from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import cars

# Create your views here.


def car(request):
    m1 = cars.objects.all()
    return render(request,'cardetails.html',{'m':m1})