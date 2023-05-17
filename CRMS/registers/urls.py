from django.contrib import admin
from django.urls import path, include
from .views import contact,loginUser,index,customerdashboard, about, recover_forgot_password, registers, Cars,tata
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("/register", views.registers, name='register'),
    path("contact.html", views.contact, name='contact'),
    path("index.html", views.index, name='home'),
    path("about.html", views.about, name='about'),
    path("contact.html", views.contact, name='contact'),
    # path("BookYourCar.html", views.Book_your_car, name='Book_your_car'),
    path("Cars.html", views.Cars, name='Cars'),
    path("login/", views.loginUser, name='login'),
    path("/login", views.logoutUser, name='login'),
    path("recover forgot password.html", views.recover_forgot_password, name='recover_forgot_password'),
    path("customer_dashboard.html", views.customerdashboard, name='customerdashboard'),
    path("tata.html", views.tata, name='tata'),
]


