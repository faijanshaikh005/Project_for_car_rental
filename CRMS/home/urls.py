from django.contrib import admin
from django.urls import path, include
from .views import car,contact,Cardetails, index, about, recover_forgot_password, Register, Cars, loginUser,customerdashboard,tata,kia,maruti,hyundai,mg,toyota,volkswagen,mahindra,honda,force,forgot
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("BookYourCar.html", views.Cardetails, name='Book_your_car'),
    path("Cars/", views.Cars, name='Cars'),
    path("recover forgot password/", views.recover_forgot_password, name='recover_forgot_password'),
    path("register.html", views.Register, name='register'),
    path("login.html", views.loginUser, name='loginUser'),
    path("customer_dashboard.html", views.customerdashboard, name='customerdashboard'),
    path("cardetails.html", views.car, name='car'),
    path("recover forgot password.html", views.forgot, name='forgot'),
    
    
    # path('', views.home, name ="home"),
    # path('login/', views.login_user, name ='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password/', views.change_password, name='change_password'),
    
    path("tata.html", views.tata, name='tata'),
    path("kia.html", views.kia, name='kia'),
    path("mahindra.html", views.mahindra, name='mahindra'),
    path("hyundai.html", views.hyundai, name='hyundai'),
    path("maruti.html", views.maruti, name='maruti'),
    path("force.html", views.force, name='force'),
    path("mg.html", views.mg, name='mg'),
    path("toyota.html", views.toyota, name='toyota'),
    path("volkswagen.html", views.volkswagen, name='volkswagen'),
    path("honda.html", views.honda, name='honda'),
 ]