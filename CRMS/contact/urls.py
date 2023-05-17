from django.contrib import admin
from django.urls import path, include
from .views import contact, index, about,  recover_forgot_password, Register, Cars, customerdashboard
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("contact.html", views.contact, name='contact'),
    path("index.html", views.index, name='home'),
    path("about.html", views.about, name='about'),
    # path("contact.html", views.contact, name='contact'),
    # path("BookYourCar.html", views.Book_car, name='Book_your_car'),
    path("Cars.html", views.Cars, name='Cars'),
    # path("login/", views.login, name='login'),
    path("recover forgot password.html", views.recover_forgot_password, name='recover_forgot_password'),
    path("register.html", views.Register, name='register'),
    # path("login/", views.login, name='login'),
     path("customer_dashboard.html", views.customerdashboard, name='customerdashboard'),

]