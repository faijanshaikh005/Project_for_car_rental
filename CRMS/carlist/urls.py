from django.contrib import admin
from django.urls import path, include
from .views import car
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cardetails.html", views.car, name='car'),
]