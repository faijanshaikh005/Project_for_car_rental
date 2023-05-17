from django.contrib import admin
from django.urls import path, include
from login import views
from .views import loginUser,logoutUser,adminUser,homepage,index

urlpatterns = [
    path('',views.index, name="home"),
    path('/login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name="logout"),
    path('admin_login.html',views.adminUser, name="admin"),
    path('admin_homepage.html',views.homepage, name="admin"),
    # path("about/", views.about, name='about'),
    # path("contact/", views.contact, name='contact'),
    # path("services/", views.services, name='services'),
    # path("Book your car/", views.Book_your_car, name='Book_your_car'),
    # path("Cars/", views.Cars, name='Cars'),
    # path("login/", views.login, name='login'),
    # path("recover forgot password/", views.recover_forgot_password, name='recover_forgot_password'),
    # path("Register/", views.Register, name='Register'),
    # path("login/", views.login, name='login'),

]